from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen(['ping', 'host'], stdout=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_subprocess.terminate()
    result, error = global_subprocess.communicate()
    if error:
        return {"status": "failed", "error": error.decode()}
    else:
        return {"status": "completed", "output": result.decode()}