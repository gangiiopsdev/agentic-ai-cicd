from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    args = ['ping', host]
    result = await asyncio.subprocess.create_subprocess_exec(*args, stdout=subprocess.PIPE)
    return await result.stdout.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}