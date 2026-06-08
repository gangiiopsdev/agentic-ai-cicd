from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid host provided')
    return host

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', validated_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}