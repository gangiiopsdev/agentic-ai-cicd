from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen without shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def home():
    return {"status": "completed"}