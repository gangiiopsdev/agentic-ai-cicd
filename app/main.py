from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Sanitize and validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return await safe_ping(host)