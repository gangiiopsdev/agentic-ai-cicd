from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return True
    except subprocess.CalledProcessError as e:
        print(e)
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "message": "Ping failed or command injection detected."}
    return {"status": "completed"}