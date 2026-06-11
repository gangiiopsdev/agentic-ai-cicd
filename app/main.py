from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = shlex.quote(host)
    command_parts = ['ping', safe_host]
    result = execute_command(command_parts)
    return {'status': 'completed', 'result': result}