from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}