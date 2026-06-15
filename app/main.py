from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = f"ping {host}"
    output = execute_command(command)
    return {'status': 'completed', 'output': output}

def is_valid_host(host: str):
    # Add your validation logic here, e.g., check if the host is in a whitelist
    return True