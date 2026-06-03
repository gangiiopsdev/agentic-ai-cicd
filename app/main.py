from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    if not host.isalnum():
        return None, 'Invalid input'
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return None, f'Ping failed with error: {error.decode()}'
        return output.decode(), None
    except Exception as e:
        return None, str(e)

app = FastAPI()

@app.get('/ping')
async def ping(host: str):
    output, error_message = await safe_ping(host)
    if error_message:
        return {'status': 'error', 'message': error_message}
    return {'status': 'completed', 'output': output}