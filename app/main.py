from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await output.communicate()
    except Exception as e:
        return None

@app.get("/ping")
async def ping(host: str):
    result = await safe_ping(host)
    if result is not None:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": "Ping failed or host unreachable"}