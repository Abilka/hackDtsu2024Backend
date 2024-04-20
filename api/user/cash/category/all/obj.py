import dataclasses


@dataclasses.dataclass
class GetCategory:
    id: int
    name: str
    picture: str