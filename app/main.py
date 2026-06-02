from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape any special characters in the host input
        command = ['ping', shlex.quote(host)]
        output = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)