from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent path traversal and other issues
    sanitized_host = host.replace('.', '')
    if '.' in sanitized_host:
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}