from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
destination = host.strip().replace(' ', '')
if destination:
    try:
        result = await asyncio.create_subprocess_exec('ping', destination, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode == 0:
            return {'status': 'success', 'output': output.decode()}
        else:
            return {'status': 'failure', 'error': error.decode()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)