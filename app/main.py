from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation for alphanumeric or IP address
    if not host.strip().isalnum() and not host.strip('0123456789.-').startswith('.'):  # Basic validation for alphanumeric or IP address
        return {'status': 'invalid_host'}
    args = shlex.split(f'ping -c 1 {host}')  # Use specific options to mitigate risks
    subprocess.run(args, check=True)  # Use subprocess.run for better control and error handling
    return {'status': 'completed'}