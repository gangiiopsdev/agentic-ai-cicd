from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_check_output(command_parts):
        try:
            output = subprocess.check_output(command_parts, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid host name')
        # Use shlex.split to safely split the command parts
        command_parts = ['ping', f'--{host}']
        return SafeSubprocess.safe_check_output(command_parts)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}