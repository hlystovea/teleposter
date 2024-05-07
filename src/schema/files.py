from pydantic import BaseModel


class File(BaseModel):
    file_unique_id: str
