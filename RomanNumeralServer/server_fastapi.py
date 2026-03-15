from fastapi import FastAPI, HTTPException
from roman import to_roman, to_arabic

app = FastAPI()


@app.get("/to_roman/{number}")
def convert_to_roman(number: int):
    try:
        return {"input": number, "roman": to_roman(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/to_arabic/{roman}")
def convert_to_arabic(roman: str):
    try:
        return {"input": roman, "arabic": to_arabic(roman)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
