from fastapi import FastAPI
import subprocess
import shlex
global subprocess_check_output
def subprocess_check_output(*popenargs, **kwargs):
    kwargs['stdout'] = subprocess.PIPE
    process = subprocess.Popen(*popenargs, **kwargs)
    output, _ = process.communicate()
    return output
global safe_subprocess_run
def safe_subprocess_run(*popenargs, **kwargs):
    kwargs['check'] = True
    return subprocess_check_output(*popenargs, **kwargs)
app = FastAPI()
def sanitize_input(user_input):
    if not all(c.isalnum() or c in [',', '.', ' '] for c in user_input): raise ValueError('Invalid input')
@app.get("/ping")
def ping(host: str): try:
        sanitized_host = shlex.quote(host)
        output = safe_subprocess_run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}