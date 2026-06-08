from fastapi import FastAPI
import subprocess
from shlex import quote

global app
app = FastAPI()

async def ping(host: str):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    try:
        result = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}