from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize and validate the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)