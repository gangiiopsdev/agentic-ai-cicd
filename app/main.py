from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {"status": "completed", "result": result}