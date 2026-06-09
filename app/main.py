from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

async def safe_ping(host):
    if not host.strip():
        return 'Invalid host'
    safe_host = shlex.quote(host)
    result = await asyncio.create_subprocess_exec('ping', '-c', '1', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        return f'Error: {error.decode()}'
    return output.decode()

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {'status': 'completed', 'output': output}