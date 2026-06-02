from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return None

@app.get("/ping")
def ping(host: str):
    result = secure_ping(host)
    if result is not None:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": "Ping command failed"}