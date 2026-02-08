from dataclasses import dataclass
from datetime import date

@dataclass
class Session:
    date: date
    duration: int
    focus: str = "No Focus"
    notes: str | None = None
    id: int | None = None