from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Use subprocess.run without shell=True for better security
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        ping_safe(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}