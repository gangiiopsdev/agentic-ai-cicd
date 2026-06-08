from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.list2cmdline([host])
        try:
            output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    if not SafeSubprocess.is_safe_input(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafeSubprocess.ping(host)

@staticmethod
def is_safe_input(input_str: str) -> bool:
    safe_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.')
    return all(char in safe_chars for char in input_str)