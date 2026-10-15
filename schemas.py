from pydantic import BaseModel, EmailStr, Field, ConfigDict




class UserCreate(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    id: int
    name: str | None
    age: int | None
    email: str | None

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    published_year: int | None = Field(default=None, ge=0)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float
    published_year: int | None

    model_config = ConfigDict(from_attributes=True)