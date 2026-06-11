from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        output = await asyncio.subprocess.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise subprocess.CalledProcessError(output.returncode, 'ping', stderr=stderr)
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)