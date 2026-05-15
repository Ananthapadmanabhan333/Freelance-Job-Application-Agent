import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Lumina | Autonomous Freelance OS",
  description: "Enterprise-grade autonomous freelance acquisition platform.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} antialiased bg-[#050505] text-white`}>
        <div className="fixed inset-0 bg-[radial-gradient(circle_at_50%_50%,_rgba(0,112,243,0.05),transparent_50%)] pointer-events-none" />
        <div className="relative z-10 min-h-screen">
          {children}
        </div>
      </body>
    </html>
  );
}
