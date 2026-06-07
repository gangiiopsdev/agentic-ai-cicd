from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_host(host: str):
    return {'result': ping(host)}