from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_subprocess(command_parts):
    try:
        result = await asyncio.create_subprocess_exec(*command_parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command_parts, output=error)
        return output.decode()
    except asyncio.TimeoutError:
        raise subprocess.TimeoutExpired(timeout=5)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command_parts = shlex.split(f'ping -c 4 {host}')
        output = await safe_subprocess(command_parts)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}