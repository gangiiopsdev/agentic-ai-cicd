from fastapi import FastAPI
import subprocess
global_args = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    global_args.append(host)
    try:
        result = subprocess.run(global_args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}