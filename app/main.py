from fastapi import FastAPI
import subprocess
import shlex
def run_command(command_parts):
    full_command = [shlex.quote(part) for part in command_parts]
    try:
        result = subprocess.run(full_command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'stdout': e.output, 'stderr': e.stderr, 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    if not all(part.isalnum() for part in command_parts):
        raise ValueError('Invalid input detected in command parts')
    return run_command(command_parts)

# Preventive controls:
# 1. Validate and sanitize user input.
# 2. Use parameterized commands instead of shell=True or shell=False if not required.
# 3. Limit the set of allowed commands to known safe ones.