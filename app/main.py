from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get("/ping")
def execute_ping(host: str):
    return ping(host)