from pydantic import BaseModel
from typing import List

class TwoSumInput(BaseModel):
    nums: List[int]
    target: int

class TwoSumOutput(BaseModel):
    indices: List[int]
