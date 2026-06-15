from fastapi import FastAPI
import subprocess
import shlex
global pinger
pinger = subprocess.Popen(['ping', '-c', '1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = shlex.quote(host)
    pinger.stdin.write(f'{safe_host}
')
    pinger.stdin.close()
    stdout, stderr = pinger.communicate()
    return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}