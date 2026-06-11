from fastapi import FastAPI
import subprocess

get_output = lambda cmd: subprocess.run(cmd.split(), capture_output=True, text=True)

def safe_get_output(cmd):
    if not isinstance(cmd, str) or '&&' in cmd or ';' in cmd or '|' in cmd:
        raise ValueError('Unsafe command detected')
    return get_output(cmd)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_get_output(f'ping {host}')
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}