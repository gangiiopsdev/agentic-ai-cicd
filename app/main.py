from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def execute_command(command):
    args = shlex.split(command)
    return await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        result = await execute_command(f"ping {host}")
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}