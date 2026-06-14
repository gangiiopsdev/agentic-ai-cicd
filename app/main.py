from fastapi import FastAPI
import subprocess
global process

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global process
    try:
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode('utf-8'), "error": error.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.on_event("shutdown")
def stop_process():
    if process:
        process.terminate()
        process.wait()