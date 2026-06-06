from fastapi import FastAPI
import asyncio

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)