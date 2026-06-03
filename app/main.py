from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'stderr': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to escape command parts
    command_parts = shlex.split(f'ping {host}')
    result = safe_subprocess(command_parts)
    if 'error' in result:
        return {'status': 'failed', **result}
    return result