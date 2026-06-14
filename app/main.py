from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate input
    if not host or 'ping' in host.lower():
        raise ValueError('Invalid input')

    app = FastAPI()

    @app.get('/ping')
    def ping(host: str):
        args = shlex.split(f'ping {shlex.quote(host)}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}

    return app