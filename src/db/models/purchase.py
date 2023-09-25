from datetime import date

from sqlalchemy.orm import Mapped

from db.models import BaseModel


class Purchase(BaseModel):

    __tablename__ = 'purchase'

    order_guid: Mapped[int]
    order_num: Mapped[str]
    date_open: Mapped[date]
    date_close: Mapped[date]
    code_MP: Mapped[int]
    client_code: Mapped[int]
    contact_client_code: Mapped[int]
    vehicle_code: Mapped[int]
    purchase_type_guid: Mapped[int]
    status: Mapped[str]
    request_reason_id: Mapped[str]
    recommendation: Mapped[str]
