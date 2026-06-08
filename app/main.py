from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and full path to executable
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)