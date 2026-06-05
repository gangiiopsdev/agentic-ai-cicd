from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ') 

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent code injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', escape_shell_argument(host)], check=True, capture_output=True)
    return {'status': 'completed'}