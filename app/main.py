from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Define allowed hosts or implement proper validation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout,
            "errors": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)