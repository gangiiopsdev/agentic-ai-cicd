from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run instead of shell=True
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}