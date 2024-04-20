import dataclasses
import datetime


@dataclasses.dataclass
class CashOperation:
    date: datetime.datetime
    price: float
    reason: str
    inn: int
    category_id: int

