from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run with args parameter
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'result': result}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return await ping(host)
    except Exception as e:
        return {'error': str(e)}