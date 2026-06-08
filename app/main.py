from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return shlex.quote(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        output = subprocess.run(['ping', '-c 1', escaped_host], capture_output=True, text=True, timeout=5, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}