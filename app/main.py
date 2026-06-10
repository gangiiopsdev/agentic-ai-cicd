from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

def safe_exec(command, *args, **kwargs):
    full_command = [command] + list(args)
    sanitized_command = [shlex.quote(arg) for arg in full_command]
    result = subprocess.run(sanitized_command, capture_output=True, text=True, check=False)
    return result

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = safe_exec('ping', sanitized_host)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': str(output.stderr)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}