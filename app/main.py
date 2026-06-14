from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Input validation
    if not host or len(host) > 255:
        raise ValueError('Invalid host')

    command = ['ping', '-c', '1', host]
    process = await asyncio.create_subprocess_exec(*command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = await ping(host)
        return {"status": "completed", "output": result[0]}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}