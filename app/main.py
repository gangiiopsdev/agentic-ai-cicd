from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to the function
    if not host.isalnum():
        return {"status": "error", "error": "Invalid input"}
    return safe_ping(host)