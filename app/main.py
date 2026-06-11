from fastapi import FastAPI
import asyncio

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    return ping(host)