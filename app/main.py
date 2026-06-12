from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
async def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode()}