from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    try:
        # Validate host input to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}