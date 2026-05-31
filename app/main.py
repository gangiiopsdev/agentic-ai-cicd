from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement sanitization logic here
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}