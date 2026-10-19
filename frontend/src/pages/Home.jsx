import { site } from '../data/sample'

export default function Home() {
  return (
    <section className="page hero">
      <div className="avatar">
        {site.photo ? <img src={site.photo} alt={site.name} /> : <div>Your photo</div>}
      </div>
      <div className="hero__text">
        <p className="eyebrow">{site.role}</p>
        <h1>Hi, I am {site.name}</h1>
        {site.intro.map((p, i) => <p key={i} className="lead">{p}</p>)}
      </div>
    </section>
  )
}