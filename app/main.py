from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return shlex.quote(input_string)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '-c 1', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}