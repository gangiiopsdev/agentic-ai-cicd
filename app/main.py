from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return "Invalid host"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)