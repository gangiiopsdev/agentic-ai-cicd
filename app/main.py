from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    command = ['ping', host]
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