from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}