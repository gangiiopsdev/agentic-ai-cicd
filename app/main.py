from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}