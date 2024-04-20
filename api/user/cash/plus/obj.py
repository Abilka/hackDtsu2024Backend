import dataclasses


@dataclasses.dataclass
class CashOperation:
    card_hash: str
    price: float
    inn: int

