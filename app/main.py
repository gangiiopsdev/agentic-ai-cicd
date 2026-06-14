from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)