from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

class SafeSubprocess:
    @staticmethod
def safe_execute(command, args):
        if not all(arg.isalnum() for arg in args):
            raise ValueError('Invalid input')
        return subprocess.run([command] + args, capture_output=True, text=True, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = SafeSubprocess.safe_execute('ping', [host])
        return {'result': result.stdout}
    except ValueError as e:
        return {'error': str(e)}