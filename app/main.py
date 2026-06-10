from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}