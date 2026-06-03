from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        # Sanitize the host input to prevent shell injection
        args = ['ping', shlex.quote(host)]
        result = await subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    try:
        # Sanitize the host input to prevent shell injection
        args = ['ping', shlex.quote(host)]
        result = await subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}