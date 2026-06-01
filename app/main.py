from fastapi import FastAPI
import subprocess

app = FastAPI()

def _run_command(command: str, args: list) -> None:
    try:
        subprocess.run([command] + args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Command failed with error: {e.stderr}')

@app.get('/ping')
def ping(host: str):
    # Safer implementation
    _run_command('ping', [host])
    return {'status': 'completed'}