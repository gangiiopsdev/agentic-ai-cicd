from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in hostname)

@app.get('/ping')
def ping(host: str):
    try:
        if not is_valid_hostname(host):
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', f'{host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'stderr': str(ve)}