from fastapi import FastAPI
import subprocess
global_lock = threading.Lock()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_lock.acquire()
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "result": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
    finally:
        global_lock.release()