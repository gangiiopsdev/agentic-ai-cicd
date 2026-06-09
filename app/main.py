from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    if host.strip() and '@' not in host:
        args = ['ping', shlex.quote(host)]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode('utf-8')}
    else:
        raise ValueError('Invalid hostname provided')
@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return response
    except ValueError as e:
        return {'error': str(e)}, 400