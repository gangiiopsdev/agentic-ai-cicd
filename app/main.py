from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in '.-')
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}