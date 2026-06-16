from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await output.stdout.read().decode()
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return {'status': 'completed', 'result': safe_ping(host)}

# Preventive control to validate the host input
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add more valid hosts as needed
    return any(h in host for h in allowed_hosts)