from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)