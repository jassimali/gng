from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer,Float


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=False
    )

    name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    password_hash: Mapped[str | None] = mapped_column(
        "pass",
        String(255),
        nullable=True
    )


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    published_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )