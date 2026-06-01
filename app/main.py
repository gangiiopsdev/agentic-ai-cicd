from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with check=True and text=True
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping(host: str):