from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex.quote to safely escape the host input
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}