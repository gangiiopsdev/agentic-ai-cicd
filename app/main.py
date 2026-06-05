from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': (await result.stderr.read()).decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)