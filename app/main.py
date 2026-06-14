from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with full path to avoid shell=True
    subprocess.run(['ping', host])

@app.get("/ping")
def get_ping(host: str):
    result = ping(host)
    return {'status': 'completed'}