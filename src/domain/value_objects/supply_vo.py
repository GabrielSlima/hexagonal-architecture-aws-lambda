from src.domain.value_objects.price_vo import PriceVO
from datetime import datetime


class SupplyVO:
    def __init__(self, start_day: datetime, end_day: datetime, submarket: str, source: str, volume: float, price: PriceVO) -> None:
        self.start_day=start_day
        self.end_day=end_day
        submarket=submarket
        source=source
        volume=volume
        price=price
