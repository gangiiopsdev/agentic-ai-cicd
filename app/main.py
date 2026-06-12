from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Constructing the ping command safely without using shell=True
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)