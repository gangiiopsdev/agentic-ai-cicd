from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use a list for the command arguments to avoid shell injection risks
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "result": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}