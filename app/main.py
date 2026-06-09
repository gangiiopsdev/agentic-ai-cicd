from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host before using it in a command
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual list of allowed hosts
    if host not in allowed_hosts:
        return 'Host is not allowed'
    # Use check_output instead of run to capture the output directly
    command = ['ping', host]
    try:
        result = subprocess.check_output(command, cwd='/safe/directory', text=True)
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'
    return result

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    result = safe_ping(request.host)
    return {'status': 'completed', 'output': result}