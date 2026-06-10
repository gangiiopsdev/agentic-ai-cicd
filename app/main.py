from fastapi import FastAPI
import subprocess
import re
import shlex
import asyncio

async def safe_ping(host):
    try:
        # Sanitize input by validating host format
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        result = await asyncio.create_subprocess_exec(
            'ping', '-c', '1', shlex.quote(host), capture_output=True, text=True
        )
        await result.wait()
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    return result