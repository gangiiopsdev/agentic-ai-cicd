from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement a proper input sanitization function here
    return ''.join(c for c in input_string if c.isalnum())

@app.get="/"
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
async def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', *sanitized_host.split()]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}