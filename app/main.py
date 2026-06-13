from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = await safe_ping(host)
        if result.returncode == 0:
            return {"status": "completed"}
        else:
            return {"status": "failed", "error": "Ping command failed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}