from fastapi import FastAPI
import subprocess
def safe_subprocess(command: list) -> str:
    try:
        result = subprocess.check_output(command, timeout=5)
        return result.decode('utf-8')
    except (subprocess.CalledProcessError, TimeoutExpired) as e:
        return None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using check_output with shell=False and input validation
    try:
        if not host.strip().replace('.', '').isnumeric():
            raise ValueError('Invalid host format')
        command = ['ping', '-c', '1', host]
        result = safe_subprocess(command)
        if result is None:
            return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}