from fastapi import FastAPI
import re
import shlex

def is_safe_hostname(hostname):
    return re.match(r'^[a-zA-Z0-9_]+$', hostname) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        args = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}