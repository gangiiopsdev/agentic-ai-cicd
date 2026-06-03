from fastapi import FastAPI
import subprocess
import shlex
global app, host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }