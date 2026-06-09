from fastapi import FastAPI
import asyncio

app = FastAPI()

async def ping(host: str):
    result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)