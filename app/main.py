from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    # Use a safer method to execute commands, avoiding shell=True and subprocess.call()
    command_parts = shlex.split(f'ping -c 1 {host}')  # Limit ping count for security
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional security measures can be added here