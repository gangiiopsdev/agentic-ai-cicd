from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Sanitize host input before using it in the command
        sanitized_host = shlex.quote(host)
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)