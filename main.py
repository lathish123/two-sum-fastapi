from fastapi import FastAPI
from model import TwoSumInput, TwoSumOutput
from logic import two_sum

app = FastAPI()

@app.post("/two-sum", response_model=TwoSumOutput)
def solve(data: TwoSumInput):
    return {"indices": two_sum(data.nums, data.target)}
