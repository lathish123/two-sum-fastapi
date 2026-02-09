from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from dsa.two_sum import two_sum
from dsa.max_element import max_element

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- Two Sum --------
class TwoSumInput(BaseModel):
    nums: List[int]
    target: int

@app.post("/two-sum")
def two_sum_api(data: TwoSumInput):
    result = two_sum(data.nums, data.target)
    return {"indices": result}

# -------- Max Element --------
class MaxInput(BaseModel):
    nums: List[int]

@app.post("/max-element")
def max_element_api(data: MaxInput):
    result = max_element(data.nums)
    return {"result": result}

