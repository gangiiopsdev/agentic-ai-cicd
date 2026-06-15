from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex.split to safely split command arguments
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500