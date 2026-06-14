from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)