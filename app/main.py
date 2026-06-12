from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}