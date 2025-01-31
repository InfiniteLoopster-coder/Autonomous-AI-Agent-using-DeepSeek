from fastapi import FastAPI
from api.routes import summarize, schedule

app = FastAPI()

app.include_router(summarize.router, prefix="/summarize")
app.include_router(schedule.router, prefix="/schedule")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
