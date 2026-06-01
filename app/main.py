from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a safe method
    args = shlex.split(f"ping {host}")
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "error": None
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "output": None,
            "error": str(e)
        }