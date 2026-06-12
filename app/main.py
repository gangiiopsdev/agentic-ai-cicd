from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host):
    command_parts = shlex.split('ping {}', host)
    try:
        result = await asyncio.create_subprocess_exec(*command_parts, capture_output=True, text=True)
        return await result.stdout()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = await safe_ping(host)
    return {"status": "completed", "response": response}