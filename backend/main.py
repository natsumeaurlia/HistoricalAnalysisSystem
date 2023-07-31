from typing import Optional, List
from fastapi import FastAPI, Query
from pydantic import BaseModel
import investpy
import pandas as pd
from datetime import datetime

class EconomicCalendar(BaseModel):
    id: str
    date: str
    time: str
    zone: str
    currency: Optional[str]
    importance: Optional[str]
    event: str
    actual: Optional[str]
    forecast: Optional[str]
    previous: Optional[str]

app = FastAPI()

def convert_date_format(date: str) -> str:
    # yyyymmdd形式の日付をdatetimeオブジェクトに変換
    date_object = datetime.strptime(date, "%Y%m%d")
    # datetimeオブジェクトをdd/mm/yyyy形式の文字列に変換
    converted_date = date_object.strftime("%d/%m/%Y")
    return converted_date

@app.get("/economic_calendar", response_model=List[EconomicCalendar], description="Retrieve economic calendar data from Investpy.")
async def get_economic_calendar(
                                time_zone: Optional[str] = Query("GMT +9:00", description="Time zone in GMT +/- hours:minutes format."),
                                from_date: Optional[str] = Query(None, alias="from", description="Start date in YYYYMMDD format."),
                                to_date: Optional[str] = Query(None, alias="to", description="End date in YYYYMMDD format."),
):
    # 入力された日付が存在する場合、日付を変換
    if from_date:
        from_date = convert_date_format(from_date)
    if to_date:
        to_date = convert_date_format(to_date)
    data = investpy.economic_calendar(time_zone=time_zone, from_date=from_date, to_date=to_date)
    # JSON responseに変換可能な形式に変換
    return data.to_dict(orient="records")

