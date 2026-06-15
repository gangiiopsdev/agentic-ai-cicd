from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "completed", "result": "failure", "error": str(e)}
    except Exception as e:
        return {"status": "completed", "result": "error", "error": str(e)}