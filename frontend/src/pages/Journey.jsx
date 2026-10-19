import TrackCard from '../components/TrackCard'
import { tracks } from '../data/sample'

export default function Journey() {
  return (
    <section className="page">
      <p className="eyebrow">My journey</p>
      <h1>Three tracks, one direction</h1>
      <p className="lead">Choose a track to see how my learning started and where I am now.</p>
      <div className="card-grid">
        {tracks.map((t) => <TrackCard key={t.slug} track={t} to={`/journey/${t.slug}`} />)}
      </div>
    </section>
  )
}