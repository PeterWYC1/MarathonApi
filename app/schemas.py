from pydantic import BaseModel

class PageRequest(BaseModel):
    page: int = 1
