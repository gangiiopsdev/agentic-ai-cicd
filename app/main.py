from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        if not host or len(host) > 256:
            raise ValueError('Invalid host input')
        args = shlex.split(f'ping -c 4 {shlex.quote(host)}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()

@app.get('/')</div>
<div class="description">
    return {'message': 'Agentic Self-Healing Pipeline'}
</div>

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(shlex.quote(host))