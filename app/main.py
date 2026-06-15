from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
async def ping_async(host: str):
    result = await ping(host)
    return result