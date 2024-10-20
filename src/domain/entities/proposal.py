from typing import List
from datetime import datetime
from src.domain.value_objects.supply_vo import SupplyVO
from src.domain.entities.contract import Contract


class Proposal:
    def __init__(self, counterparty_id: str, start_date, end_date: datetime, supplies: List[SupplyVO]) -> None:
        self.counterparty_id=counterparty_id
        self.start_date=start_date
        self.end_date=end_date
        self.supplies=supplies
