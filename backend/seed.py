from sqlalchemy import select

from app.database import SessionLocal
from app.models import Profile, Track

TRACKS = [
    ("software-developer", "Software developer", "Building full-stack applications"),
    ("cloud-engineer", "Cloud engineer", "Azure, CI/CD and infrastructure"),
    ("cybersecurity", "Cybersecurity", "Labs, CTFs and secure design"),
]


def main():
    with SessionLocal() as db:
        for slug, name, summary in TRACKS:
            if not db.scalar(select(Track).where(Track.slug == slug)):
                db.add(Track(slug=slug, name=name, summary=summary))

        if not db.scalar(select(Profile)):
            db.add(Profile(full_name="Paul Marvin"))

        db.commit()
    print("Seed complete")


if __name__ == "__main__":
    main()