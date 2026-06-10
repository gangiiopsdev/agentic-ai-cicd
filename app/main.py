from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stderr=subprocess.STDOUT, timeout=10)
        result = await output.communicate()
        return {'status': 'completed', 'output': result[0].decode()}
    except (subprocess.CalledProcessError, asyncio.TimeoutError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Add logic to check if the host is safe (e.g., whitelist, blacklist)
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts