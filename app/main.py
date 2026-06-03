from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

async def execute_ping(host):
    validate_host(host)
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input before using it in the subprocess
    sanitized_host = shlex.quote(host)
    return await execute_ping(sanitized_host)