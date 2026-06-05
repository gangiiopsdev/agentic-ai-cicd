from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Enhanced validation to prevent command injection
        if '@' in host or '&&' in host or ';' in host or '|' in host or '!' in host or '`' in host or '&' in host or '$' in host or '\' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}