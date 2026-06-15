from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list for the command
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):