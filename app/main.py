from fastapi import FastAPI
import subprocess
import shlex

def escape_shell_input(input_string):
    return ''.join(shlex.quote(c) for c in input_string)

app = FastAPI()
global_env = {}  # Ensure all environment variables are safe

@app.get('/ping')
def ping(host: str):
    try:
        host = escape_shell_input(host)
        args = shlex.split('ping -c 1 {}'.format(host))
        subprocess.run(args, check=True, env=global_env, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}