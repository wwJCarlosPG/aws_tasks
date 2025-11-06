from pydantic import BaseModel, Field
from typing import Optional, Literal
class Task(BaseModel):
    task_id: Optional[str] = Field(default=None, description="Unique identifier for the task")
    title: str = Field(description="Title of the task")
    description: str = Field(description="Description of the task")
    status: Literal['pending', 'in_progress', 'completed'] = Field(description="Status of the task")