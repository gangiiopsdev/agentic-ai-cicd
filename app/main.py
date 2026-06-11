from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Using safe and secure method to ping without shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}