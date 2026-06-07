from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Example of safe input validation
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'invalid host'}
    subprocess.call(['ping', host])  # Using list avoids shell=True vulnerability
    return {'status': 'completed'}