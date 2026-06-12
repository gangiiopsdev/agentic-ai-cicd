from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host and all(char.isalnum() or char in ('.', '-') for char in host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}