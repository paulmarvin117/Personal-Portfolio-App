import TrackCard from '../components/TrackCard'
import { tracks } from '../data/sample'

export default function Projects() {
  return (
    <section className="page">
      <p className="eyebrow">Projects</p>
      <h1>Selected work</h1>
      <p className="lead">Choose a track to see the projects I built.</p>
      <div className="card-grid">
        {tracks.map((t) => <TrackCard key={t.slug} track={t} to={`/projects/${t.slug}`} />)}
      </div>
    </section>
  )
}