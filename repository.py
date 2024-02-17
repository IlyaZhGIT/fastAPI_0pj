from sqlalchemy import select
from database import new_sessions, TaskOrm
from schemas import Task, TaskAdd


class TaskRepository():
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_sessions() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
    
    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_sessions() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [Task.model_validate(task) for task in task_models]
            return tasks

