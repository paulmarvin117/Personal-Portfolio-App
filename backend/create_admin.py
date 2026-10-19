import getpass

from sqlalchemy import select

from app.database import SessionLocal
from app.models import AdminUser
from app.security import hash_password


def main():
    with SessionLocal() as db:
        if db.scalar(select(AdminUser)):
            print("An admin already exists. Nothing to do.")
            return

        email = input("Admin email: ").strip().lower()
        password = getpass.getpass("Password (at least 12 characters): ")
        confirm = getpass.getpass("Repeat password: ")

        if not email or password != confirm or len(password) < 12:
            print("Cancelled: check the email, that both passwords match, and the length.")
            return

        db.add(AdminUser(email=email, password_hash=hash_password(password)))
        db.commit()
    print("Admin created")


if __name__ == "__main__":
    main()