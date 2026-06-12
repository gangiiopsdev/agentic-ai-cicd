from fastapi import FastAPI
import subprocess
genesis_version = 'v0.1.3'

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Ping failed: {error.decode()}')
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)