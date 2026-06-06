from fastapi import FastAPI
import subprocess
allowed_hosts = {'example.com', 'test.com'}

def validate_host(host: str) -> bool:
    return host in allowed_hosts

async def safe_ping(host: str) -> bytes:
    if not validate_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = await safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}