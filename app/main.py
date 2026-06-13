from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command, args):
    try:
        completed_process = subprocess.run([command] + args, check=True, capture_output=True, text=True)
        return completed_process.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr), 1

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    result, status = run_command('ping', [host])
    return {'status': status, 'result': result}