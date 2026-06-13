from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        # Ensure the host input is valid and does not contain malicious commands
        if '||' in host or '&' in host or ';' in host:
            raise ValueError('Invalid input detected')
        safe_host = shlex.quote(host)
        output = await asyncio.to_thread(subprocess.check_output, ['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)