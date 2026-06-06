from fastapi import FastAPI
import subprocess

async def run_ping(host: str):
    # Secure implementation using subprocess.run for better control and error handling
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            return f'Ping failed: {stderr.decode().strip()}'
        return stdout.decode().strip()
    except Exception as e:
        return f'Ping failed: {str(e)}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await run_ping(host)