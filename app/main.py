from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e.output.decode().strip())

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}