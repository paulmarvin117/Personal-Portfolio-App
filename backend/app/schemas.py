from datetime import date

from pydantic import BaseModel, ConfigDict, Field, field_validator


def check_url(value: str | None) -> str | None:
    # Blocks things like "javascript:..." that could run code when a link is clicked
    if value and not value.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")
    return value


class MediaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    kind: str
    blob_name: str
    caption: str


class JourneyEntryIn(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    body: str = Field(default="", max_length=10000)
    happened_on: date | None = None
    sort_order: int = 0


class JourneyEntryOut(JourneyEntryIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
    media: list[MediaOut] = []


class ProjectIn(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str = Field(default="", max_length=10000)
    live_url: str | None = Field(default=None, max_length=500)
    repo_url: str | None = Field(default=None, max_length=500)

    _urls = field_validator("live_url", "repo_url")(check_url)


class ProjectOut(ProjectIn):
    model_config = ConfigDict(from_attributes=True)
    id: int
    media: list[MediaOut] = []


class CertificateIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    issuer: str = Field(default="", max_length=150)
    issued_on: date | None = None
    credential_url: str | None = Field(default=None, max_length=500)

    _url = field_validator("credential_url")(check_url)


class CertificateOut(CertificateIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TrackStats(BaseModel):
    certificates: int
    photos: int
    projects: int


class TrackSummary(BaseModel):
    slug: str
    name: str
    summary: str
    stats: TrackStats


class TrackDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    slug: str
    name: str
    summary: str
    journey_entries: list[JourneyEntryOut]
    projects: list[ProjectOut]
    certificates: list[CertificateOut]


class ProfileIn(BaseModel):
    full_name: str = Field(min_length=1, max_length=100)
    headline: str = Field(default="", max_length=200)
    bio: str = Field(default="", max_length=10000)


class ProfileOut(ProfileIn):
    model_config = ConfigDict(from_attributes=True)
    photo_blob_name: str | None = None