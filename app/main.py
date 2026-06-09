from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None

@app.get("/ping")
def ping(host: str):
    output = _ping(host)
    if output is not None:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": "Failed to execute ping command."}