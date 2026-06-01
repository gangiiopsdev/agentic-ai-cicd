from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with error handling
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        raise Exception(e.stderr)