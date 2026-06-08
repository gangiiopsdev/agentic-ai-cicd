from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
descriptor = {'host': host}
subprocess.run(['ping', '{host}'], check=True, env=descriptor)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)