from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}