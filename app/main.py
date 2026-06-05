from fastapi import FastAPI
import subprocess

app = FastAPI()

async def execute_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.replace('.', '').isdigit():
            return {'status': 'failed', 'error': 'Invalid host'}
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)