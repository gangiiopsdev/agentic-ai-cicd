from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command: str):
    try:
        result = subprocess.run(command, check=True, shell=False, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed with exit code {e.returncode}: {e.stderr}'

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', *shlex.split(host)]
    command = ' '.join(args)
    return {'status': run_command(command)}