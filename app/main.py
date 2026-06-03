from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation using subprocess.run with input validation
    if not host or '@' in host or ';' in host:
        raise ValueError('Invalid hostname')
    try:
        args = ['ping', host]
        result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}