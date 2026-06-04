from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isdigit():
        return "Invalid input"
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode().strip()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}