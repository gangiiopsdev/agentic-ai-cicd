from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.strip() or len(host) > 256:
        raise ValueError('Invalid host name')

app = FastAPI()

async def ping(host: str):
    validate_host(host)
    try:
        output = await asyncio.to_thread(subprocess.run, ['ping', '-c', '4', subprocess.list2cmdline([host])], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    validate_host(host)
    return ping(host)