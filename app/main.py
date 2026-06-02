from fastapi import FastAPI
import subprocess
git
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}