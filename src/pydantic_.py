import typing as tp

from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    postcode: str = Field(..., min_length=4, max_length=10)


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, description="User's full name")
    email: str
    is_active: bool = True
    tags: tp.List[str] = []  # default empty list
    scores: tp.Optional[tp.List[float]] = None  # optional field
    address: Address


# Example data
input_data = {
    "id": 1,
    "name": "Isabel",
    "email": "isabel@example.com",
    "tags": ["admin", "beta-tester"],
    "scores": ["abc", 92.3],
    "address": {"street": "42 Galaxy Ave", "city": "Moonville", "postcode": "12345"},
}

user = User(**input_data)

input_data["address"]
user.address


class User:

    def __init__(self, name):
        self.name = name


user = User("Isabel")
user.name
