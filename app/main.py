from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    try:
        host_parts = shlex.split(host)
        if len(host_parts) != 1 or not host_parts[0].isnumeric():
            return {'status': 'error', 'message': 'Invalid input'}
        subprocess.run(['ping'] + host_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except shlex.Error as e:
        return {'status': 'error', 'message': f'Input parsing error: {e}'}
    return {'status': 'completed'}