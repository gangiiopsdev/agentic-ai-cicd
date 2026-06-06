from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call with shell=True
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'result': True}
    except subprocess.CalledProcessError as e:
        return {'result': False, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}