from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error executing ping: {e}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)