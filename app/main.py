from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input to prevent command injection
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        args = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the input
        subprocess.run(args, check=True, input=None)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}