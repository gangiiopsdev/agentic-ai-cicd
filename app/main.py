from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def validate_host(host):
    allowed_hosts = ["example.com", "test.net"]
    return host in allowed_hosts

async def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")

    result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return stdout.decode(), stderr.decode()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe_endpoint(host: str):
    stdout, stderr = await ping_safe(host)
    return {
        "status": "completed",
        "stdout": stdout,
        "stderr": stderr
    }