from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isnumeric() or len(host) > 15:
        return {"status": "failed", "error": "Invalid host input"}
    return secure_ping(host)