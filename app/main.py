from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using check_output to avoid shell=True and execute command safely
        args = shlex.split(f'ping -c 1 {host}')  # Limiting the number of pings for security
        subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

# Add a function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., IP address format check
    return True