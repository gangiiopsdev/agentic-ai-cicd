from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    return {'result': ping(host)}