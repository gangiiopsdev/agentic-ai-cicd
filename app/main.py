from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def run_ping(host: str):
    cmd = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*cmd, capture_output=True, text=True)
        return await result.stdout.read()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = run_ping(host)
    return {"status": "completed", "response": response}