from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        completed_process = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return completed_process.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'result': 'Invalid input'}
    # Sanitize the host parameter to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    command = ['ping', sanitized_host]
    result = execute_safe_command(command)
    return {'status': 'completed', 'result': result}