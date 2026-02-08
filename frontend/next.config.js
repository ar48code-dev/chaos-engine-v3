/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
        // 'domains' is deprecated. 'remotePatterns' is more secure and required for Next 16+
        remotePatterns: [
            {
                protocol: 'http',
                hostname: 'localhost',
            },
            {
                protocol: 'https',
                hostname: '**.googleusercontent.com', // Allows Gemini/Imagen images
            },
        ],
    },
    // The specific devIndicators options you had were removed in Next 16.
    // We use the new simplified format instead.
    devIndicators: {
        appIsrStatus: false, // This is now handled automatically but safe to keep
    },
}

module.exports = nextConfig
