from fastapi import FastAPI
import subprocess
global_subprocess_args = ['ping', None]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    global_subprocess_args[1] = host
    try:
        result = subprocess.run(global_subprocess_args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}