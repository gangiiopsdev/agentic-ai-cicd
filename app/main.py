from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Safe implementation using subprocess.run and avoiding shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}