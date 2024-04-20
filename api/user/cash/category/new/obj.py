import dataclasses


@dataclasses.dataclass
class GetCategory:
    name: str
    picture: str