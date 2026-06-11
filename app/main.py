from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return output.decode().strip()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {"status": "completed", "output": output}