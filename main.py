from fastapi import FastAPI

from celery.result import AsyncResult
from datetime import datetime, timedelta
from celery_worker import ScheduledTask


app = FastAPI()


@app.get("/schedule-task")
def schedule_task():
    # Schedule the task to run every 5 minutes
    eta = datetime.now() + timedelta(minutes=5)
    result = ScheduledTask().apply_async(eta=eta)
    return {"message": f"Task scheduled with ID: {result.id}", "eta": eta}


# API endpoint to check the task status
@app.get("/task-status/{task_id}")
def task_status(task_id: str):
    result = AsyncResult(task_id)
    print(result)

    if result.ready():
        return {"status": "Task completed", "result": result.result}
    else:
        return {"status": "Task still running"}
