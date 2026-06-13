from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Sanitize the host input to avoid command injection
    safe_host = re.sub(r'[^a-zA-Z0-9-.]', '', host)
    result = await app.state.executor.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return result

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'status': ping(host)}
    except Exception as e:
        return {'error': str(e)}, 400