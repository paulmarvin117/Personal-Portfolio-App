export const site = {
  name: 'Your Name',
  initials: 'YN',
  role: 'Software developer · Cloud engineer · Cybersecurity',
  photo: null, // later: '/images/me.jpg'
  intro: [
    'Write two or three sentences about who you are and what you do.',
    'Say what drives you and what you are working towards.',
  ],
}

export const tracks = [
  {
    slug: 'software-developer',
    name: 'Software developer',
    icon: 'code',
    tagline: 'Building full-stack applications',
    image: null, // later: '/images/software.jpg'
    stats: { certificates: 2, photos: 12, projects: 5 },
    journey: {
      intro: 'How my software development journey started and where it is now.',
      milestones: [
        { date: '2023', title: 'Started learning', text: 'What I began with and why.' },
        { date: '2024', title: 'First real project', text: 'What I built and learned.' },
      ],
    },
    projects: [
      { title: 'Project one', description: 'A short description of what it does.', link: '#', image: null },
    ],
  },
  {
    slug: 'cloud-engineer',
    name: 'Cloud engineer',
    icon: 'cloud',
    tagline: 'Azure, CI/CD and infrastructure',
    image: null,
    stats: { certificates: 1, photos: 8, projects: 3 },
    journey: {
      intro: 'How my cloud engineering journey started and where it is now.',
      milestones: [{ date: '2024', title: 'Started with Azure', text: 'First steps in the cloud.' }],
    },
    projects: [
      { title: 'Project one', description: 'A short description of what it does.', link: '#', image: null },
    ],
  },
  {
    slug: 'cybersecurity',
    name: 'Cybersecurity',
    icon: 'shield',
    tagline: 'Labs, CTFs and secure design',
    image: null,
    stats: { certificates: 1, photos: 6, projects: 2 },
    journey: {
      intro: 'How my cybersecurity journey started and where it is now.',
      milestones: [{ date: '2025', title: 'First security labs', text: 'What I practised.' }],
    },
    projects: [
      { title: 'Project one', description: 'A short description of what it does.', link: '#', image: null },
    ],
  },
]