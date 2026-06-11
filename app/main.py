from fastapi import FastAPI
import subprocess
def shell_quote(cmd):
    return ' '.join(subprocess.list2cmdline([arg]) for arg in cmd)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host parameter to ensure it does not contain malicious input
        if not host.isalnum() or '..' in host or '\' in host or '/' in host:
            raise ValueError('Invalid host value')
        output = subprocess.run([shell_quote(['ping', host])], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'error': str(e)}