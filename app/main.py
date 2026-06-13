from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Validate the host input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Using regex for more comprehensive validation
            raise ValueError('Invalid host name')
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)