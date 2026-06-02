from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input for ping command')
    
    args = ['ping', '-c', '4', host]  # Use specific parameters to avoid shell injection
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
async def ping(host: str):
    return await safe_ping(host)