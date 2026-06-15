from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize host input to prevent shell injection
        safe_host = shlex.quote(host)
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, text=True, shell=False)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}