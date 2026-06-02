from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def get_ping():
    return {"status": "completed"}