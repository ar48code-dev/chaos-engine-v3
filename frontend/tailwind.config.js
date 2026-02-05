/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/**/*.{js,ts,jsx,tsx,mdx}",
        "./pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./components/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                background: "#0a0e27",
                primary: "#00f2ff",
                secondary: "#7c3aed",
                accent: "#ff6b35",
                success: "#10b981",
                danger: "#ef4444",
                text: "#e2e8f0",
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                mono: ['Fira Code', 'monospace'],
                orbitron: ['Orbitron', 'sans-serif'],
            },
            animation: {
                'pulse-fast': 'pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'spin-slow': 'spin 3s linear infinite',
            },
        },
    },
    plugins: [],
}
