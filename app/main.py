from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        host = ''.join(filter(str.isalnum, host))
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return await safe_ping(host)