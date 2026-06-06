from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        try:
            return subprocess.run(command, check=True, stdout=subprocess.PIPE, shell=False, **kwargs)
        except subprocess.CalledProcessError as e:
            raise Exception(f'Command {command} failed: {e}')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = ''.join(c for c in host.strip() if c.isdigit())
        if host.isdigit():
            result = SafeSubprocess.run(['ping', '-c', '4', shlex.quote(host)], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}