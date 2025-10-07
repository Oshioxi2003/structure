import '../styles/globals.scss'

export const metadata = {
  title: 'Edu Project',
  description: 'Educational platform',
}

export default function RootLayout({ children }) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  )
}
