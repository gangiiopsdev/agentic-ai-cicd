from fastapi import FastAPI
import subprocess

async def execute_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)