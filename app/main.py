from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command, *args):
    try:
        output = subprocess.check_output([command] + list(args), stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    return run_command('ping', host)