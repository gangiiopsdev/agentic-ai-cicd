from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.strip().isdigit():
        return "Invalid host"
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}