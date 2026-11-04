import { useState } from 'react'

const number = (import.meta.env.VITE_WHATSAPP_NUMBER || '').replace(/\D/g, '')
const waLink = `https://wa.me/${number}?text=${encodeURIComponent(
  'Hi, I found your portfolio and would like to make an inquiry.'
)}`

export default function Contact() {
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')
  const [status, setStatus] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    setStatus('Sending…')
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/api/contact`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, message }),
      })
      if (!res.ok) throw new Error('failed')
      setStatus('Message sent. Thank you!')
      setEmail('')
      setMessage('')
    } catch {
      setStatus('Could not send right now. Please try WhatsApp instead.')
    }
  }

  return (
    <section className="page narrow">
      <p className="eyebrow">Reach out</p>
      <h1>Let us talk</h1>
      <p className="lead">Send a message or start a WhatsApp chat directly.</p>

      <form onSubmit={handleSubmit} className="form">
        <input type="email" required placeholder="Your email" value={email}
          onChange={(e) => setEmail(e.target.value)} />
        <textarea required rows="6" maxLength="2000" placeholder="Your message" value={message}
          onChange={(e) => setMessage(e.target.value)} />
        <div className="form__row">
          <button type="submit" className="btn fill">Send message</button>
          <a href={waLink} target="_blank" rel="noopener noreferrer" className="btn">Chat on WhatsApp</a>
        </div>
        {status && <p className="status">{status}</p>}
      </form>
    </section>
  )
}