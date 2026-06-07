from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts instead of sanitizing the input
        if host in ['example.com', 'another.example.com']:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "error", "error": "Invalid host"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)