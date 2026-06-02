from fastapi import FastAPI
import subprocess
global args
args = {"ping": ["-c", "4"]}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(["ping", *args[host]], capture_output=True, text=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500