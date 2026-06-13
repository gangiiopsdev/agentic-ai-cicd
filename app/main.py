from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not all(char.isalnum() or char in '-.' for char in host):
        raise ValueError('Invalid host')
    result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}