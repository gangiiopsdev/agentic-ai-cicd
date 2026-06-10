from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation with full path and shell=False
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Ping initiated'}