from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        for arg in command:
            if not isinstance(arg, str) or ';' in arg or '&' in arg or '|' in arg:
                raise ValueError('Invalid argument detected in command')
        try:
            result = subprocess.run(command, capture_output=True, check=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isprintable() or ';' in host or '&' in host or '|' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    try:
        result = SafeSubprocess.run(command)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}