from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid characters in hostname')
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}