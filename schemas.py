from pydantic import BaseModel, ConfigDict


class TaskAdd(BaseModel):
    name: str
    description: str | None = None


class Task(TaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TaskId(BaseModel):
    ok: bool = True
    task_id: int
