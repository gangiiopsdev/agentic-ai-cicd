from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shlex.quote to escape user input
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    return {'status': 'completed', 'output': safe_subprocess_call(command)}