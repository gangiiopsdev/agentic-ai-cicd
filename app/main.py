from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if '@' in host or '%' in host:
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}