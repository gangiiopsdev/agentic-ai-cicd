from fastapi import FastAPI
import ipaddress
import subprocess

app = FastAPI()

async def execute_ping(host):
    try:
        # Validate the host as an IP address or hostname
        ipaddress.ip_address(host)
    except ValueError:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return await execute_ping(host)