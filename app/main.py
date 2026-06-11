from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host: str):
    # Safe implementation using Popen and shell=False
    command = ['ping', host]
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    return output, error

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Execute the ping command safely
    result = await execute_ping(host)
    return {"status": "completed", "output": result[0].decode(), "error": result[1].decode() if result[1] else None}