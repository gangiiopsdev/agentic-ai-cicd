from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping():
    subprocess.call(["ping", "8.8.8.8"])
    return {"status": "completed"}