from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/calc_gpa")


@router.get("/{input_string}", response_class=PlainTextResponse)
async def calc_gpa(input_string: str):
    grades = [float(i) for i in input_string.split(",")]
    gpa = sum(grades) / len(grades)

    # format string to truncate and zero-pad to 2dp
    return "{0:.2f}".format(gpa)
