from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Ensure the host input does not contain potentially harmful characters or patterns
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host format'}

    try:
        output = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', output.stderr.decode())
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await ping(host)