from fastapi import FastAPI
import subprocess
import shlex
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input before using it in the command
    sanitized_host = shlex.quote(host)
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}