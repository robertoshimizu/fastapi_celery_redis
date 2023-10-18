import uvicorn
from fastapi import FastAPI
from app.celery.celery_app import compute_fibonacci, long_fake_api

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to fastapi-celery!"}

@app.post("/fake_wait/{n}")
async def start_computation(n: int):
    # Sending the computation to the Celery worker
    task = long_fake_api.delay(n)
    return {"task_id": task.id, "status": "Computation started!"}

@app.get("/get-result/{task_id}")
async def get_result(task_id: str):
    try:
        task = long_fake_api.AsyncResult(task_id)
        if task.state == "PENDING":
            return {"status": "Computation is still in progress!"}
        elif task.state == "SUCCESS":
            return {"status": "Computation complete!", "result": task.result}
        else:
            return {"status": "Error with task!", "task_state": task.state, "task_info": str(task.info)}
    except Exception as e:
        return {"status": "Server Error!", "error_detail": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)