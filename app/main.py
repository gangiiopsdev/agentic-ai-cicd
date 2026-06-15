from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stderr=subprocess.STDOUT, timeout=5)
        return (await output.communicate())[0].decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return run_ping(host)