from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host or any(char in host for char in '!@#$%^&*()_+={}[]|;:,.<>?/\`~'):
        raise ValueError('Invalid host format')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        args = ['ping'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}