from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run with check_output and splitting the host to prevent injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"status": "failed", "error": str(e)}