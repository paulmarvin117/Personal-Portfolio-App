from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from ..database import get_db
from ..models import JourneyEntry, Profile, Project, Track
from ..schemas import ProfileOut, TrackDetail, TrackStats, TrackSummary

router = APIRouter(prefix="/api", tags=["public"])


def load_options():
    # Load related rows in a few queries, not one query per row
    return (
        selectinload(Track.journey_entries).selectinload(JourneyEntry.media),
        selectinload(Track.projects).selectinload(Project.media),
        selectinload(Track.certificates),
    )


def photo_count(track: Track) -> int:
    items = [*track.journey_entries, *track.projects]
    return sum(1 for item in items for m in item.media if m.kind == "image")


@router.get("/profile", response_model=ProfileOut)
def get_profile(db: Session = Depends(get_db)):
    profile = db.scalar(select(Profile))
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/tracks", response_model=list[TrackSummary])
def list_tracks(db: Session = Depends(get_db)):
    tracks = db.scalars(select(Track).options(*load_options()).order_by(Track.id)).all()
    return [
        TrackSummary(
            slug=t.slug,
            name=t.name,
            summary=t.summary,
            stats=TrackStats(
                certificates=len(t.certificates),
                photos=photo_count(t),
                projects=len(t.projects),
            ),
        )
        for t in tracks
    ]


@router.get("/tracks/{slug}", response_model=TrackDetail)
def get_track(slug: str, db: Session = Depends(get_db)):
    track = db.scalar(select(Track).where(Track.slug == slug).options(*load_options()))
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    detail = TrackDetail.model_validate(track)
    detail.journey_entries.sort(key=lambda e: (e.sort_order, e.happened_on or date.min))
    detail.projects.sort(key=lambda p: p.id, reverse=True)
    return detail