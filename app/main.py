from fastapi import FastAPI
import subprocess

async def secure_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = secure_ping(host)
    return {"status": "completed", "output": response}