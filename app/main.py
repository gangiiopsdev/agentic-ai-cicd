from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: list[str]):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e.stderr}'

app = FastAPI()
def is_valid_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Validate the input to prevent injection attacks
    valid_inputs = ['localhost', '127.0.0.1']
    for arg in command:
        if arg not in valid_inputs:
            raise ValueError('Invalid argument in command')
    result = SafeSubprocess.safe_call(['ping', host])
    return {'status': 'completed', 'result': result}