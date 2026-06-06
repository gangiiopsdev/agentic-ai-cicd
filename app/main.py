from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400