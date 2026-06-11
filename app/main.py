from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and use of safe shell=True
    if all(c.isalnum() or c in ('.', '-', '_') for c in host):
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "reason": "Invalid hostname"}