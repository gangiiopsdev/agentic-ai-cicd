from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}

@app.get("/ping")
def ping_route(host: str):  # Rename function to avoid naming conflict
    return ping(host)