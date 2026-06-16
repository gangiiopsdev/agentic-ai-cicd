from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        subprocess.run(['ping', shlex.quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):    
    return await safe_ping(host)