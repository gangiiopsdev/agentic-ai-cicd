from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of shell=True
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}