from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    ping_command = ['ping', host]
    subprocess.run(ping_command, check=True)

@app.get="/ping")
def ping(host: str):    return {'status': 'completed'}