from fastapi import FastAPI
import subprocess
import shlex
global ping_command
canonical_ping_command = ['ping', '{}']

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

def run_command(host):
    sanitized_host = sanitize_input(host)
    command = canonical_ping_command.copy()
    command[1] = shlex.quote(sanitized_host)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

@app.get("/ping")
def ping(host: str):
    try:
        result = run_command(host)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return result