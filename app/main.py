from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and argument unpacking
        result = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)