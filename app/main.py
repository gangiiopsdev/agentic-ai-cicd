from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return None

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is not None:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": "Ping failed or host unreachable"}