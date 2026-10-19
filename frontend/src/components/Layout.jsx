import { Suspense } from 'react'
import { NavLink, Outlet } from 'react-router-dom'
import { site } from '../data/sample'

const links = [
  { to: '/', label: 'Who am I' },
  { to: '/journey', label: 'My journey' },
  { to: '/projects', label: 'Projects' },
  { to: '/contact', label: 'Reach out' },
]

export default function Layout() {
  return (
    <>
      <nav className="navbar">
        <NavLink to="/" className="brand">
          <span className="logo">{site.initials}</span>
          {site.name}
        </NavLink>
        {links.map((l) => (
          <NavLink key={l.to} to={l.to} end={l.to === '/'} className="link">
            {l.label}
          </NavLink>
        ))}
      </nav>
      <main>
        <Suspense fallback={<p className="loading">Loading…</p>}>
          <Outlet />
        </Suspense>
      </main>
      <footer className="footer">© {new Date().getFullYear()} {site.name}</footer>
    </>
  )
}