from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result.stdout}