import dataclasses


@dataclasses.dataclass
class Privileges:
    privileges_prefix: str
    name: str
    legend: str
    history: str