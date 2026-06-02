from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', '--', host]  # Add -- to prevent command injection
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Invalid input'
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app = FastAPI()

@app.get('/ping')
async def ping(host: str):
    response = await safe_ping(host)
    return {'status': 'completed', 'response': response}