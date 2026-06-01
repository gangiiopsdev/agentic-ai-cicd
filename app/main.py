from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}