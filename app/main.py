from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Simple host validation, replace with more robust validation as needed
    return ''.join(c for c in host if c.isalnum() or c in '-._')

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = sanitize_host(host)
        output = subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}