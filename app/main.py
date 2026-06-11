from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, check=True)
        return (await result.stdout.read()).decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    return run_ping(host)