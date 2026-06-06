from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode()}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)