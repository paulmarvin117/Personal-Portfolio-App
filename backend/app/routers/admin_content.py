from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..deps import get_current_admin
from ..models import Certificate, JourneyEntry, Profile, Project, Track
from ..schemas import (
    CertificateIn, CertificateOut, JourneyEntryIn, JourneyEntryOut,
    ProfileIn, ProfileOut, ProjectIn, ProjectOut,
)

# The router-level dependency protects EVERY route in this file
router = APIRouter(
    prefix="/api/admin", tags=["admin content"], dependencies=[Depends(get_current_admin)]
)


def get_or_404(db: Session, model, item_id: int):
    item = db.get(model, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


def track_or_404(db: Session, slug: str) -> Track:
    track = db.scalar(select(Track).where(Track.slug == slug))
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


def apply(item, data: BaseModel):
    for key, value in data.model_dump().items():
        setattr(item, key, value)


@router.put("/profile", response_model=ProfileOut)
def update_profile(data: ProfileIn, db: Session = Depends(get_db)):
    profile = db.scalar(select(Profile))
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    apply(profile, data)
    db.commit()
    db.refresh(profile)
    return profile


# ---- Journey entries ----
@router.post("/tracks/{slug}/journey", response_model=JourneyEntryOut, status_code=201)
def create_entry(slug: str, data: JourneyEntryIn, db: Session = Depends(get_db)):
    track = track_or_404(db, slug)
    entry = JourneyEntry(track_id=track.id, **data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.put("/journey/{entry_id}", response_model=JourneyEntryOut)
def update_entry(entry_id: int, data: JourneyEntryIn, db: Session = Depends(get_db)):
    entry = get_or_404(db, JourneyEntry, entry_id)
    apply(entry, data)
    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/journey/{entry_id}", status_code=204)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db.delete(get_or_404(db, JourneyEntry, entry_id))
    db.commit()


# ---- Projects ----
@router.post("/tracks/{slug}/projects", response_model=ProjectOut, status_code=201)
def create_project(slug: str, data: ProjectIn, db: Session = Depends(get_db)):
    track = track_or_404(db, slug)
    project = Project(track_id=track.id, **data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.put("/projects/{project_id}", response_model=ProjectOut)
def update_project(project_id: int, data: ProjectIn, db: Session = Depends(get_db)):
    project = get_or_404(db, Project, project_id)
    apply(project, data)
    db.commit()
    db.refresh(project)
    return project


@router.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db.delete(get_or_404(db, Project, project_id))
    db.commit()


# ---- Certificates ----
@router.post("/tracks/{slug}/certificates", response_model=CertificateOut, status_code=201)
def create_certificate(slug: str, data: CertificateIn, db: Session = Depends(get_db)):
    track = track_or_404(db, slug)
    cert = Certificate(track_id=track.id, **data.model_dump())
    db.add(cert)
    db.commit()
    db.refresh(cert)
    return cert


@router.put("/certificates/{cert_id}", response_model=CertificateOut)
def update_certificate(cert_id: int, data: CertificateIn, db: Session = Depends(get_db)):
    cert = get_or_404(db, Certificate, cert_id)
    apply(cert, data)
    db.commit()
    db.refresh(cert)
    return cert


@router.delete("/certificates/{cert_id}", status_code=204)
def delete_certificate(cert_id: int, db: Session = Depends(get_db)):
    db.delete(get_or_404(db, Certificate, cert_id))
    db.commit()