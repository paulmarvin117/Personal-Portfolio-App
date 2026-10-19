from datetime import date, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Track(Base):
    """One of your three tracks: software developer, cloud engineer, cybersecurity."""
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True)  # used in URLs
    name: Mapped[str] = mapped_column(String(100))
    summary: Mapped[str] = mapped_column(String(300), default="")

    journey_entries: Mapped[list["JourneyEntry"]] = relationship(back_populates="track")
    projects: Mapped[list["Project"]] = relationship(back_populates="track")


class JourneyEntry(Base):
    __tablename__ = "journey_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))
    title: Mapped[str] = mapped_column(String(150))
    body: Mapped[str] = mapped_column(Text, default="")
    happened_on: Mapped[date | None]
    sort_order: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    track: Mapped["Track"] = relationship(back_populates="journey_entries")
    media: Mapped[list["MediaItem"]] = relationship(back_populates="journey_entry", cascade="all, delete-orphan")


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text, default="")
    live_url: Mapped[str | None] = mapped_column(String(500))
    repo_url: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    track: Mapped["Track"] = relationship(back_populates="projects")
    media: Mapped[list["MediaItem"]] = relationship(back_populates="project", cascade="all, delete-orphan")


class MediaItem(Base):
    """An image or video stored in Azure Blob Storage. Belongs to a journey entry OR a project."""
    __tablename__ = "media_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    kind: Mapped[str] = mapped_column(String(10))  # "image" or "video"
    blob_name: Mapped[str] = mapped_column(String(300))
    caption: Mapped[str] = mapped_column(String(200), default="")
    journey_entry_id: Mapped[int | None] = mapped_column(ForeignKey("journey_entries.id"))
    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"))

    journey_entry: Mapped["JourneyEntry | None"] = relationship(back_populates="media")
    project: Mapped["Project | None"] = relationship(back_populates="media")


class Profile(Base):
    """The 'Who am I' section. Only ever one row."""
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    headline: Mapped[str] = mapped_column(String(200), default="")
    bio: Mapped[str] = mapped_column(Text, default="")
    photo_blob_name: Mapped[str | None] = mapped_column(String(300))


class AdminUser(Base):
    """Only you. We store a password hash, never the password itself."""
    __tablename__ = "admin_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))