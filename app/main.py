from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}