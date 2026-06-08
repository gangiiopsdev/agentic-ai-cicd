from fastapi import FastAPI
import subprocess
global_params = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', host], **global_params)
    output = result.stdout.decode()
    error = result.stderr.decode()
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}