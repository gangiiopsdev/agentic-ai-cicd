from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    if '.' in host and ':' in host:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {"status": "invalid input"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr.decode()}