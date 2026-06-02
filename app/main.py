from fastapi import FastAPI
import re

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if re.match(r'^[0-9a-fA-F:.]+$', host) and host in allowed_hosts:
        args = ['ping', '-c', '1', host]  # Use ping with count to limit the number of pings
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Invalid input'

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
async def ping(host: str):
    response = await safe_ping(host)
    return {'status': 'completed', 'response': response}