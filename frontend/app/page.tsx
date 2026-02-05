"use client";

import React from 'react';

// Mock Diff View Component for "Generate Fixes"
const DiffView = ({ onClose }: { onClose: () => void }) => (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
        <div className="bg-[#0a0c1b] border border-primary/30 w-full max-w-4xl h-[80vh] rounded-xl flex flex-col relative shadow-[0_0_50px_rgba(0,242,255,0.2)]">
            <div className="flex justify-between items-center p-4 border-b border-white/10 bg-white/5 rounded-t-xl">
                <h3 className="font-orbitron text-xl text-primary">🔧 AUTOMATED_FIX_PROPOSAL :: v3.1</h3>
                <button onClick={onClose} className="text-gray-400 hover:text-white hover:rotate-90 transition-all">✖</button>
            </div>
            <div className="flex-grow flex font-fira-code text-xs overflow-hidden">
                <div className="w-1/2 p-4 border-r border-white/10 overflow-y-auto bg-red-900/10">
                    <h4 className="text-red-400 mb-2 uppercase font-bold text-center">--- ORIGINAL (Lines 10-15) ---</h4>
                    <pre className="text-red-200 opacity-70">
                        {`    def take_damage(self, amount):
        if amount > 0:
            self.hp -= amount
            # BUG: No death check!
`}
                    </pre>
                </div>
                <div className="w-1/2 p-4 overflow-y-auto bg-green-900/10">
                    <h4 className="text-green-400 mb-2 uppercase font-bold text-center">+++ AUTO-FIXED (Lines 10-18) +++</h4>
                    <pre className="text-green-300">
                        {`    def take_damage(self, amount):
        if amount > 0:
            self.hp -= amount
            # FIXED: Added death check
            if self.hp <= 0:
                self.die()
`}
                    </pre>
                </div>
            </div>
            <div className="p-4 border-t border-white/10 flex justify-end gap-3 bg-white/5 rounded-b-xl">
                <button onClick={onClose} className="px-4 py-2 rounded text-gray-300 hover:bg-white/10 transition-colors">Discard</button>
                <button onClick={onClose} className="px-6 py-2 rounded bg-primary text-black font-bold hover:shadow-[0_0_15px_rgba(0,242,255,0.6)] transition-all">
                    APPLY FIXES TO SOURCE
                </button>
            </div>
        </div>
    </div>
);

// Settings Modal Component
const SettingsModal = ({
    isOpen,
    onClose,
    apiKey,
    setApiKey
}: {
    isOpen: boolean;
    onClose: () => void;
    apiKey: string;
    setApiKey: (key: string) => void;
}) => {
    if (!isOpen) return null;
    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
            <div className="bg-[#0a0c1b] border border-primary/30 w-full max-w-md rounded-xl p-6 shadow-[0_0_50px_rgba(0,242,255,0.2)]">
                <h3 className="font-orbitron text-xl text-white mb-4">⚙️ SYSTEM_CONFIG</h3>
                <div className="space-y-4">
                    <div>
                        <label className="block text-xs text-gray-400 mb-1">GOOGLE GEMINI API KEY</label>
                        <input
                            type="password"
                            value={apiKey}
                            onChange={(e) => setApiKey(e.target.value)}
                            placeholder="Paste your AIza... key here"
                            className="w-full bg-black/50 border border-white/10 rounded p-3 text-sm text-white focus:border-primary focus:outline-none"
                        />
                        <p className="text-[10px] text-gray-500 mt-2">
                            * Your key is sent securely to the backend for this session only.
                            It allows Real AI Analysis instead of Demo Mode.
                        </p>
                    </div>
                </div>
                <div className="mt-6 flex justify-end">
                    <button
                        onClick={onClose}
                        className="px-6 py-2 rounded bg-white/10 hover:bg-white/20 text-white transition-colors"
                    >
                        Save & Close
                    </button>
                </div>
            </div>
        </div>
    );
};

// Summary Report Modal
const SummaryModal = ({
    isOpen,
    onClose,
    results,
    mode
}: {
    isOpen: boolean;
    onClose: () => void;
    results: any;
    mode?: string;
}) => {
    if (!isOpen || !results) return null;

    const totalIssues = Object.keys(results).length;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
            <div className="bg-[#0a0c1b] border border-primary/30 w-full max-w-4xl max-h-[90vh] rounded-xl flex flex-col shadow-[0_0_50px_rgba(0,242,255,0.2)] overflow-hidden">
                <div className="flex justify-between items-center p-4 border-b border-white/10 bg-white/5">
                    <div>
                        <h3 className="font-orbitron text-xl text-primary">📊 COMPREHENSIVE ANALYSIS REPORT</h3>
                        <p className="text-xs text-gray-400 mt-1">
                            {mode === 'REAL_GEMINI_AI' ? '🤖 Generated by Gemini Advanced AI' : '⚠️ Demo Mode Results'}
                        </p>
                    </div>
                    <button onClick={onClose} className="text-gray-400 hover:text-white hover:rotate-90 transition-all">✖</button>
                </div>

                <div className="flex-grow overflow-y-auto p-6">
                    {/* Executive Summary */}
                    <div className="bg-white/5 rounded-lg p-4 mb-6 border border-primary/20">
                        <h4 className="font-orbitron text-primary mb-2">EXECUTIVE SUMMARY</h4>
                        <p className="text-sm text-gray-300">
                            Analysis complete. {totalIssues} AI agent{totalIssues > 1 ? 's' : ''} identified critical findings
                            across security, performance, and code quality dimensions.
                        </p>
                    </div>

                    {/* Agent Reports */}
                    <div className="space-y-4">
                        {Object.entries(results).map(([agent, finding]: [string, any], idx) => (
                            <div key={agent} className="bg-gradient-to-r from-white/5 to-transparent rounded-lg p-4 border-l-4 border-primary/50">
                                <div className="flex items-center gap-3 mb-2">
                                    <span className="text-2xl">
                                        {agent === 'griefer' ? '💥' : agent === 'speedrunner' ? '⚡' : '🔍'}
                                    </span>
                                    <h5 className="font-orbitron text-lg text-white uppercase">{agent}</h5>
                                    <span className="text-xs bg-red-500/20 text-red-400 px-2 py-1 rounded">CRITICAL</span>
                                </div>
                                <p className="text-sm text-gray-300 ml-11">{finding}</p>
                            </div>
                        ))}
                    </div>

                    {/* Recommendations */}
                    <div className="mt-6 bg-green-500/10 rounded-lg p-4 border border-green-500/30">
                        <h4 className="font-orbitron text-green-400 mb-2">💡 RECOMMENDED ACTIONS</h4>
                        <ul className="text-sm text-gray-300 space-y-2">
                            <li>• Review all CRITICAL findings immediately</li>
                            <li>• Use "Generate Fixes" to view automated solutions</li>
                            <li>• Re-run audit after applying fixes to verify resolution</li>
                        </ul>
                    </div>
                </div>

                <div className="p-4 border-t border-white/10 flex justify-end gap-3 bg-white/5">
                    <button onClick={onClose} className="px-6 py-2 rounded bg-white/10 hover:bg-white/20 text-white transition-colors">
                        Close
                    </button>
                </div>
            </div>
        </div>
    );
};

export default function Home() {
    const [code, setCode] = React.useState('');
    const [logs, setLogs] = React.useState<string[]>([]);
    const [isAnalyzing, setIsAnalyzing] = React.useState(false);
    const [results, setResults] = React.useState<any>(null);
    const [showFixModal, setShowFixModal] = React.useState(false);
    const [activeAgent, setActiveAgent] = React.useState<string | null>(null);

    // New State for Settings
    const [showSettings, setShowSettings] = React.useState(false);
    const [apiKey, setApiKey] = React.useState('');
    const [showSummary, setShowSummary] = React.useState(false);
    const [analysisMode, setAnalysisMode] = React.useState<string>('DEMO_MOCK');
    const [bugVisual, setBugVisual] = React.useState<string | null>(null);
    const [isGeneratingVisual, setIsGeneratingVisual] = React.useState(false);

    const addLog = (msg: string) => setLogs(prev => [...prev, msg]);

    const handleClear = () => {
        setCode('');
        setLogs([]);
        setResults(null);
        setActiveAgent(null);
    };

    const handleLoadExample = () => {
        setCode(`class Player:
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, amount):
        if amount > 0:
            self.hp -= amount
            # TODO: Fix infinite health bug if amount is negative
`);
        addLog("📂 Loaded example: game_physics_v1.py");
    };

    const handleRunAudit = async () => {
        if (!code) {
            addLog("❌ ERROR: No code provided to analyze!");
            return;
        }

        setIsAnalyzing(true);
        setResults(null);
        setActiveAgent(null);
        setLogs([]); // Clear previous
        addLog("🚀 Initializing Chaos Engine V3...");
        addLog("📡 Connecting to AI Agents...");

        try {
            const response = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    code,
                    api_key: apiKey // Pass the key from UI
                }),
            });

            const data = await response.json();

            if (data.logs) {
                data.logs.forEach((l: string) => addLog(l));
            }
            setResults(data.agents);
            setAnalysisMode(data.mode || 'DEMO_MOCK');
            addLog("✨ Audit sequence finished successfully.");
            addLog("📊 Click 'View Summary' for comprehensive report.");
        } catch (error) {
            addLog("🔥 CRITICAL FAILURE: Could not connect to backend.");
            console.error(error);
        } finally {
            setIsAnalyzing(false);
        }
    };

    const handleGenerateVisual = async () => {
        if (!results) return;

        setIsGeneratingVisual(true);
        addLog("🎨 Generating visual bug report with Imagen 3...");

        try {
            // Use the griefer finding as the bug description
            const bugDesc = results.griefer || "Unknown bug";
            const bugType = bugDesc.toLowerCase().includes('crash') ? 'crash' :
                bugDesc.toLowerCase().includes('glitch') ? 'glitch' :
                    bugDesc.toLowerCase().includes('performance') ? 'performance' : 'logic';

            const response = await fetch('http://localhost:8000/generate-bug-visual', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    bug_description: bugDesc,
                    bug_type: bugType,
                    api_key: apiKey
                }),
            });

            const data = await response.json();

            if (data.status === 'success') {
                setBugVisual(data.image);
                addLog("✅ Visual bug report generated successfully!");
            } else {
                addLog(`❌ Visual generation failed: ${data.message}`);
            }
        } catch (error) {
            addLog("🔥 Failed to generate visual report");
            console.error(error);
        } finally {
            setIsGeneratingVisual(false);
        }
    };

    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-8 relative overflow-hidden">
            {showFixModal && <DiffView onClose={() => setShowFixModal(false)} />}
            <SettingsModal
                isOpen={showSettings}
                onClose={() => setShowSettings(false)}
                apiKey={apiKey}
                setApiKey={setApiKey}
            />
            <SummaryModal
                isOpen={showSummary}
                onClose={() => setShowSummary(false)}
                results={results}
                mode={analysisMode}
            />

            {/* Demo Mode Warning Banner */}
            {!apiKey && (
                <div className="fixed top-20 left-1/2 transform -translate-x-1/2 z-40 bg-yellow-500/20 border border-yellow-500/50 rounded-lg px-6 py-3 backdrop-blur-sm">
                    <p className="text-yellow-400 text-sm font-mono">
                        ⚠️ DEMO MODE: Click Settings to add API Key for Real AI Analysis
                    </p>
                </div>
            )}

            {/* Background Gradients */}
            <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
                <div className="absolute top-[-50%] left-[-20%] w-[800px] h-[800px] bg-secondary/20 rounded-full blur-[120px]" />
                <div className="absolute bottom-[-20%] right-[-10%] w-[600px] h-[600px] bg-primary/10 rounded-full blur-[100px]" />
            </div>

            <header className="z-10 w-full max-w-7xl items-center justify-between font-mono text-sm flex mb-12">
                <div className="flex items-center gap-4">
                    <div className="w-12 h-12 bg-gradient-to-br from-primary to-secondary rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(0,242,255,0.5)]">
                        <span className="text-2xl">⚡</span>
                    </div>
                    <div>
                        <h1 className="text-3xl font-orbitron font-bold text-white tracking-widest">
                            CHAOS <span className="text-primary">ENGINE</span> V3
                        </h1>
                        <p className="text-xs text-gray-400">AUTONOMOUS MULTI-AGENT GAME QA</p>
                    </div>
                </div>
                <button
                    onClick={() => setShowSettings(true)}
                    className="glass-panel px-6 py-2 rounded-full hover:bg-white/5 transition-all flex items-center gap-2 border-primary/30"
                >
                    ⚙️ Settings
                </button>
            </header>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 w-full max-w-7xl flex-grow">
                {/* Left Col: Input & Console */}
                <div className="lg:col-span-8 flex flex-col gap-6">

                    {/* Input Section */}
                    <div className="glass-panel p-1 rounded-xl relative group">
                        <div className="absolute -inset-0.5 bg-gradient-to-r from-primary to-secondary rounded-xl opacity-30 group-hover:opacity-75 blur transition duration-1000"></div>
                        <div className="relative bg-background rounded-xl p-6 h-[500px] flex flex-col">
                            <div className="flex justify-between items-center mb-4">
                                <h3 className="font-orbitron text-lg flex items-center gap-2">
                                    INPUT_SOURCE <span className="text-xs font-mono text-gray-500">[AUTO-DETECT: Python/C#/JS/C++]</span>
                                </h3>
                                <div className="flex gap-2">
                                    <button
                                        onClick={handleClear}
                                        className="px-3 py-1 text-xs bg-red-500/10 hover:bg-red-500/20 text-red-400 rounded border border-red-500/20 transition-colors flex items-center gap-1"
                                    >
                                        🗑️ Clear
                                    </button>
                                    <button
                                        onClick={handleLoadExample}
                                        className="px-3 py-1 text-xs bg-white/5 hover:bg-white/10 rounded border border-white/10 transition-colors"
                                    >
                                        Load Example
                                    </button>
                                    <button className="px-3 py-1 text-xs bg-white/5 hover:bg-white/10 rounded border border-white/10 cursor-not-allowed text-gray-500">
                                        Upload File
                                    </button>
                                </div>
                            </div>
                            <textarea
                                value={code}
                                onChange={(e) => setCode(e.target.value)}
                                className="w-full h-full bg-[#050714] text-gray-300 font-mono text-sm p-4 rounded-lg resize-none focus:outline-none focus:ring-1 focus:ring-primary/50"
                                placeholder="# Paste your game code here (Python, C#, JavaScript, C++, Java supported)&#10;# Supports up to 50K lines...&#10;&#10;class Player:&#10;    def __init__(self):&#10;        self.health = 100"
                            ></textarea>
                        </div>
                    </div>

                    {/* Console */}
                    <div className="glass-panel p-4 rounded-xl min-h-[250px] font-mono text-sm bg-black/50 border-t-4 border-primary/50">
                        <div className="flex justify-between items-center mb-2 text-gray-400 text-xs border-b border-white/10 pb-2">
                            <span>LIVE_LOGS :: {isAnalyzing ? 'RUNNING...' : 'SYSTEM_READY'}</span>
                            <span>v3.0.0-alpha</span>
                        </div>
                        <div className="flex flex-col gap-1 text-green-400/90 h-[200px] overflow-y-auto font-fira-code">
                            <p className="text-gray-500">_ Waiting for input...</p>
                            {logs.map((log, i) => (
                                <p key={i} className="animate-in fade-in slide-in-from-left-2 duration-300">
                                    {log}
                                </p>
                            ))}
                        </div>
                    </div>

                    {/* Bug Visual Display */}
                    {bugVisual && (
                        <div className="glass-panel p-4 rounded-xl bg-black/50 border-t-4 border-purple-500/50">
                            <div className="flex justify-between items-center mb-2 text-gray-400 text-xs border-b border-white/10 pb-2">
                                <span>VISUAL_BUG_REPORT :: IMAGEN_3_GENERATED</span>
                                <button
                                    onClick={() => setBugVisual(null)}
                                    className="text-red-400 hover:text-red-300"
                                >
                                    ✖ Close
                                </button>
                            </div>
                            <img
                                src={bugVisual}
                                alt="Bug Visualization"
                                className="w-full rounded-lg shadow-[0_0_30px_rgba(168,85,247,0.3)]"
                            />
                        </div>
                    )}

                </div>

                {/* Right Col: Agents & Actions */}
                <div className="lg:col-span-4 flex flex-col gap-6">

                    {/* Action Card */}
                    <div className="glass-panel p-6 rounded-xl flex flex-col gap-4">
                        <h2 className="font-orbitron text-xl mb-2">CONTROL_CENTER</h2>
                        <button
                            onClick={handleRunAudit}
                            disabled={isAnalyzing}
                            className={`w-full py-4 rounded-lg font-bold text-white shadow-[0_0_20px_rgba(255,107,53,0.4)] transition-all flex items-center justify-center gap-2
                                ${isAnalyzing ? 'bg-gray-600 cursor-wait' : 'bg-gradient-to-r from-accent to-red-500 hover:scale-[1.02]'}`}
                        >
                            {isAnalyzing ? '⏳ ANALYZING...' : '▶️ RUN CHAOS AUDIT'}
                        </button>
                        <button
                            onClick={() => setShowSummary(true)}
                            disabled={!results || isAnalyzing}
                            className={`w-full py-3 rounded-lg font-bold border flex items-center justify-center gap-2 transition-all
                                ${!results || isAnalyzing
                                    ? 'bg-white/5 text-gray-500 border-white/10 cursor-not-allowed'
                                    : 'bg-green-500/10 text-green-400 border-green-500 hover:bg-green-500/20 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]'}`}
                        >
                            📊 VIEW SUMMARY
                        </button>
                        <button
                            onClick={() => setShowFixModal(true)}
                            disabled={!results || isAnalyzing}
                            className={`w-full py-3 rounded-lg font-bold border flex items-center justify-center gap-2 transition-all
                                ${!results || isAnalyzing
                                    ? 'bg-white/5 text-gray-500 border-white/10 cursor-not-allowed'
                                    : 'bg-primary/10 text-primary border-primary hover:bg-primary/20 hover:shadow-[0_0_15px_rgba(0,242,255,0.3)]'}`}
                        >
                            🔧 GENERATE FIXES
                        </button>
                        <button
                            onClick={handleGenerateVisual}
                            disabled={!results || isAnalyzing || isGeneratingVisual}
                            className={`w-full py-3 rounded-lg font-bold border flex items-center justify-center gap-2 transition-all
                                ${!results || isAnalyzing || isGeneratingVisual
                                    ? 'bg-white/5 text-gray-500 border-white/10 cursor-not-allowed'
                                    : 'bg-purple-500/10 text-purple-400 border-purple-500 hover:bg-purple-500/20 hover:shadow-[0_0_15px_rgba(168,85,247,0.3)]'}`}
                        >
                            {isGeneratingVisual ? '⏳ GENERATING...' : '🎨 VISUAL BUG REPORT'}
                        </button>
                    </div>

                    {/* Agents */}
                    <div className="flex flex-col gap-4">
                        {['Griefer', 'Speedrunner', 'Auditor'].map((agent) => (
                            <div
                                key={agent}
                                onClick={() => results && setActiveAgent(agent)}
                                className={`glass-panel p-4 rounded-xl border-l-4 transition-all duration-300 cursor-pointer 
                                    ${activeAgent === agent ? 'bg-white/10 scale-[1.02] border-primary shadow-[0_0_15px_rgba(0,242,255,0.3)]' : 'border-gray-700 hover:border-gray-500 hover:bg-white/5'}
                                `}
                            >
                                <div className="flex justify-between items-center">
                                    <h3 className="font-orbitron text-lg text-gray-300">{agent.toUpperCase()}</h3>
                                    <div className="flex items-center gap-2">
                                        <div className={`w-2 h-2 rounded-full ${isAnalyzing ? 'bg-yellow-400 animate-ping' : results ? 'bg-green-500' : 'bg-gray-500'}`}></div>
                                        <span className="text-xs text-gray-500">{isAnalyzing ? 'BUSY' : results ? 'ONLINE' : 'IDLE'}</span>
                                    </div>
                                </div>
                                {results && (
                                    <div className={`mt-2 text-xs pt-2 border-t border-white/5 animate-in zoom-in duration-300 ${activeAgent === agent ? 'text-white' : 'text-gray-400'}`}>
                                        {activeAgent === agent ? (
                                            <div className="flex flex-col gap-2">
                                                <p className="font-bold text-primary">&gt;&gt; FULL REPORT DETECTED:</p>
                                                <p>{results[agent.toLowerCase()]}</p>
                                                <p className="text-[10px] text-gray-500 mt-2 font-mono">ID: {Math.random().toString(36).substr(2, 9)} | Latency: 42ms</p>
                                            </div>
                                        ) : (
                                            <p className="truncate">{results[agent.toLowerCase()]}</p>
                                        )}
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>

                </div>
            </div>
        </main>
    )
}
