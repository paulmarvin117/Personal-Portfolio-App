import { Link } from 'react-router-dom'
import Icon from './Icons'

export default function TrackCard({ track, to }) {
  const { name, tagline, icon, image, stats } = track
  return (
    <Link to={to} className="track-card">
      <div className="track-card__media">
        {image ? (
          <img src={image} alt={name} loading="lazy" />
        ) : (
          <div className="track-card__fallback"><Icon name={icon} size={56} /></div>
        )}
      </div>
      <div className="track-card__body">
        <h3>{name}</h3>
        <p>{tagline}</p>
        <ul className="stats">
          <li><b>{stats.certificates}</b><span>Certificates</span></li>
          <li><b>{stats.photos}</b><span>Photos</span></li>
          <li><b>{stats.projects}</b><span>Projects</span></li>
        </ul>
      </div>
    </Link>
  )
}