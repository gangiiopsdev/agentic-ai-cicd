from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}