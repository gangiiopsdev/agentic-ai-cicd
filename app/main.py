from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe way to ping without using subprocess
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)