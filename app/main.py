from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input"}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)