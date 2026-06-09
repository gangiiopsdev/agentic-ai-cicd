from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation with input validation and use of check_output instead of call
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get('/ping')
def ping_endpoint(host: str):
    return await ping(host)

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}