from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_run(command: list) -> str:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.output}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', host]
    result = SafeSubprocess.safe_run(command)
    return {'status': 'completed', 'output': result}

def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts