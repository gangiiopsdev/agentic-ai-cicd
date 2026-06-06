from fastapi import FastAPI
import subprocess
call_args = ['ping', host]
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(call_args)
    return {"status": "completed"}