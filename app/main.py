from fastapi import FastAPI
import asyncio

app = FastAPI()

def async_ping(host: str) -> dict:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, ping, host)
    return result

async def ping(host: str) -> dict:
    if host == 'localhost' or host.startswith('127.0.0.'):  # Example of a safe check, customize as needed
        try:
            process = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            output, error = await process.communicate()
            if process.returncode == 0:
                return {'status': 'completed', 'output': output.decode().strip()}
            else:
                return {'status': 'failed', 'error': error.decode().strip()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping_endpoint(host: str):
    return async_ping(host)