from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if host.isalnum():
        await asyncio.create_subprocess_exec('ping', host)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping_endpoint(host: str):  # Renamed function to avoid naming conflict with the existing function
    return ping(host)