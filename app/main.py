from fastapi import FastAPI
import subprocess
import shlex

class CommandExecutionException(Exception):
    pass

app = FastAPI()

def validate_input(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'error': 'Invalid input'}, 400

    try:
        # Use subprocess.run with shell=False and proper argument handling
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise CommandExecutionException(f'Failed to execute command: {e}') from e