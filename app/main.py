from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return "Invalid host"
    try:
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "response": response.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)