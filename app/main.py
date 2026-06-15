from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}