from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum():
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {"status": "completed", "output": output}