from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in '-.' for c in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        command = ['ping', shlex.quote(host)]
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}