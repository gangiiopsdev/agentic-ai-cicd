from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of safe hosts or implement more sophisticated validation logic
    return host in ['example.com', 'localhost']

async def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)