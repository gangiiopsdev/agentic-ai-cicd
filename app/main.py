from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}