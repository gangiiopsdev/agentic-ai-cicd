from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_ping_command(host):
    return ['ping', host]

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(create_ping_command(host), shell=False)

    return {"status": "completed"}