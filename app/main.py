from fastapi import FastAPI
import subprocess
global app
app = FastAPI()
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not all(c.isalnum() or c in ' -.' for c in host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
@app.get("/ping")
def ping_with_validation(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ' -.' for c in host):
        raise ValueError('Invalid hostname')
    return ping(host)