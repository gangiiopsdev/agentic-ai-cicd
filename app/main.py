from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host or '&&' in host or ';' in host:
        return None  # Prevent potential command injection
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output is None:
        return {"status": "invalid input"}
    return {"status": "completed", "output": output}