from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to safely quote the host argument
        command = ['ping', *shlex.split(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except Exception as e:
        return {'error': str(e)}