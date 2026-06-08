from fastapi import FastAPI
import subprocess
import shlex
globally_whitelisted_hosts = {'example.com', 'another-example.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        try:
            result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed: {e.stderr}'}, 500
    else:
        return {'error': 'Host not allowed'}, 403