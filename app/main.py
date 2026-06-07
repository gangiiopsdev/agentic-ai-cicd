from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "completed", "result": "failure", "error": str(e)}
    except Exception as e:
        return {"status": "completed", "result": "error", "error": str(e)}