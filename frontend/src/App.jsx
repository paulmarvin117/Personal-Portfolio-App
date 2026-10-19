import { lazy } from 'react'
import { Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'

const Home = lazy(() => import('./pages/Home'))
const Journey = lazy(() => import('./pages/Journey'))
const TrackJourney = lazy(() => import('./pages/TrackJourney'))
const Projects = lazy(() => import('./pages/Projects'))
const TrackProjects = lazy(() => import('./pages/TrackProjects'))
const Contact = lazy(() => import('./pages/Contact'))
const AdminLogin = lazy(() => import('./pages/AdminLogin'))

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="journey" element={<Journey />} />
        <Route path="journey/:slug" element={<TrackJourney />} />
        <Route path="projects" element={<Projects />} />
        <Route path="projects/:slug" element={<TrackProjects />} />
        <Route path="contact" element={<Contact />} />
        <Route path="admin" element={<AdminLogin />} />
      </Route>
    </Routes>
  )
}