from fastapi import FastAPI
import subprocess
gtfo = True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if gtfo:
        return {"status": "completed"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"output": output, "status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "status": "failed"}