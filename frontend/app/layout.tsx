import type { Metadata } from 'next'
import { Inter, Orbitron, Fira_Code } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' })
const orbitron = Orbitron({ subsets: ['latin'], variable: '--font-orbitron' })
const firaCode = Fira_Code({ subsets: ['latin'], variable: '--font-fira-code' })

export const metadata: Metadata = {
    title: 'Chaos Engine V3',
    description: 'Autonomous Multi-Agent Game QA System',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
            <body className={`${inter.variable} ${orbitron.variable} ${firaCode.variable} font-sans`}>
                {children}
            </body>
        </html>
    )
}
