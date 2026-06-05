from fastapi import FastAPI
import subprocess
import shlex

global_subprocess_args = ['ping']

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        # Sanitize the input to prevent injection attacks
        safe_host = shlex.quote(host)
        result = subprocess.run(global_subprocess_args + [safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}