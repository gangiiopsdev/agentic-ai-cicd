from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=False)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'completed', 'result': ping(host)}