import type { Metadata } from "next";
import "../styles/globals.css";

export const metadata: Metadata = {
  title: "LOTA Security Verity",
  description: "Evidence-driven security posture assessment",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
