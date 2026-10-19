import { Link, useParams } from 'react-router-dom'
import { tracks } from '../data/sample'

export default function TrackJourney() {
  const { slug } = useParams()
  const track = tracks.find((t) => t.slug === slug)

  if (!track) {
    return (
      <section className="page">
        <h1>Track not found</h1>
        <Link to="/journey" className="back">← All tracks</Link>
      </section>
    )
  }

  return (
    <section className="page">
      <Link to="/journey" className="back">← All tracks</Link>
      <p className="eyebrow">Learning journey</p>
      <h1>{track.name}</h1>
      <p className="lead">{track.journey.intro}</p>

      <ol className="timeline">
        {track.journey.milestones.map((m) => (
          <li key={m.title}>
            <span className="timeline__date">{m.date}</span>
            <h3>{m.title}</h3>
            <p>{m.text}</p>
          </li>
        ))}
      </ol>

      <h2>Photos and videos</h2>
      <div className="media-grid">
        <div className="media-slot">Image</div>
        <div className="media-slot">Video</div>
        <div className="media-slot">Image</div>
      </div>
    </section>
  )
}