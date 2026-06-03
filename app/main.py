from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse
global_params = dict(encoding='utf-8', text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = shlex.split(f'ping {host}')
        subprocess.check_output(command, **global_params, stderr=subprocess.STDOUT)
        return JSONResponse(content={"status": "completed"}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": str(e.output)}, status_code=500)