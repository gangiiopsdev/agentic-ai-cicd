from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use a list instead of shell=True for safety
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        command = ['ping', host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": await safe_ping(host)}