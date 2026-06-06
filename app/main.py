from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using a list for the command arguments
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}