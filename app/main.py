from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use safe method to avoid shell injection
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}