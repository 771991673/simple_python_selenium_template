from pydantic import BaseModel, Field, PyObject, typing
from pydantic.typing import Optional
import datetime


class OHLCVSchema(BaseModel):
    symbol: str
    dt: datetime.datetime
    dataID: Optional[str]
    o: float
    h: float
    l: float
    c: float
    v: float
    action: int