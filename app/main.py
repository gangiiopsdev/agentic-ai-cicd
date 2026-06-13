from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": result.stderr}