from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call for better security
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "output": None}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}