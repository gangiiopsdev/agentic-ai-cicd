from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        result, _ = run_command(args)
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}