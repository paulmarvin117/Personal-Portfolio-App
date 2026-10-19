from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..deps import get_current_admin
from ..models import AdminUser
from ..security import DUMMY_HASH, create_access_token, verify_password

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = db.scalar(select(AdminUser).where(AdminUser.email == form.username.strip().lower()))
    valid = verify_password(form.password, admin.password_hash if admin else DUMMY_HASH)
    if not admin or not valid:
        # One vague message, so it never reveals whether the email exists
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return {"access_token": create_access_token(admin.email), "token_type": "bearer"}


@router.get("/me")
def me(admin: AdminUser = Depends(get_current_admin)):
    return {"email": admin.email}