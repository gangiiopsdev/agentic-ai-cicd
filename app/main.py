from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed", "output": result}