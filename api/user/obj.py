import dataclasses


@dataclasses.dataclass
class ReturnUser:
    user_id: int
    username: str