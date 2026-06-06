from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run with a list instead of a string for safety
    subprocess.run(['ping', host])

@app.get("/ping")
def ping(host: str):