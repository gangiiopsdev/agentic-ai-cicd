from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, timeout=10)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}