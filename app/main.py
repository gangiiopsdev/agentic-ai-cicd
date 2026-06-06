from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in '.-' for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}