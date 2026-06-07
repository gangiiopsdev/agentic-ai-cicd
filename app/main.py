from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and avoiding shell=True
    subprocess.run(['ping', host], check=True)

def home(request):
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_endpoint(host: str):
    await ping(host)
    return {'status': 'completed'}