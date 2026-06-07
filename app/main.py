from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safe implementation using subprocess.run with args tuple
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = run_ping(host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}