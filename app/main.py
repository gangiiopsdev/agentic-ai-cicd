from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_whitelisted_hosts:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}