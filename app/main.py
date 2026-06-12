from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in safe_chars)

cmd = ['ping'] + shlex.split(sanitize_input(host))
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}