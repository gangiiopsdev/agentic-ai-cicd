from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    if not isinstance(input_string, str) or '&&' in input_string or ';' in input_string:
        raise ValueError('Invalid input')
    return input_string
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}