from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def run_command(command):
    # Sanitize command using shlex.split
    safe_command = shlex.split(' '.join(command))
    result = await asyncio.create_subprocess_exec(*safe_command, check=True, capture_output=True, text=True)
    return result.stdout.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}