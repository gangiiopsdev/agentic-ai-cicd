from fastapi import FastAPI
import subprocess
import shlex
def run_safe_subprocess(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.isalnum() or len(host) > 64:
            raise ValueError("Invalid host")
        output = run_safe_subprocess('ping', shlex.quote(host))
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}