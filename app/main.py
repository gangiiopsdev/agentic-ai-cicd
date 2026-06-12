from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_', '@', '+'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        args = ["ping", shlex.quote(sanitized_host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}