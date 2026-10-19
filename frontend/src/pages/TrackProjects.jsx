import { Link, useParams } from 'react-router-dom'
import { tracks } from '../data/sample'

export default function TrackProjects() {
  const { slug } = useParams()
  const track = tracks.find((t) => t.slug === slug)

  if (!track) {
    return (
      <section className="page">
        <h1>Track not found</h1>
        <Link to="/projects" className="back">← All tracks</Link>
      </section>
    )
  }

  return (
    <section className="page">
      <Link to="/projects" className="back">← All tracks</Link>
      <p className="eyebrow">Projects</p>
      <h1>{track.name}</h1>
      <div className="card-grid">
        {track.projects.map((p) => (
          <article key={p.title} className="project">
            <div className="track-card__media">
              {p.image ? <img src={p.image} alt={p.title} loading="lazy" /> : <div className="track-card__fallback">Image</div>}
            </div>
            <div className="track-card__body">
              <h3>{p.title}</h3>
              <p>{p.description}</p>
              <a href={p.link} target="_blank" rel="noopener noreferrer" className="text-link">
                Visit project →
              </a>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}