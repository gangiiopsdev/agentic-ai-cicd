from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Ensure host input is sanitized before using it in the command
        safe_host = shlex.quote(host)
        result = subprocess.run(shlex.split(f'ping {safe_host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}