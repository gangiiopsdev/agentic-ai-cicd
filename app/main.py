from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

async def safe_ping(host: str):
    try:
        # Sanitize host input using shlex.quote
        cmd = ['ping', shlex.quote(host)]
        output = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_bytes, _ = await output.communicate()
        return {'status': 'completed', 'output': output_bytes.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}

@app.get(
    "/",
    summary="Agentic Self-Healing Pipeline"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    summary="Ping a host"
)
def ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'error', 'output': 'Invalid host'}
    return await safe_ping(host)