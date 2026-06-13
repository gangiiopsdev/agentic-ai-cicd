from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using args instead of shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/" República
}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}