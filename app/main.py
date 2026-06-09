from fastapi import FastAPI
import subprocess
def escape_argument(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_argument(host)
    try:
        result = subprocess.run(['ping', '-c 1', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}