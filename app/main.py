from fastapi import FastAPI
import subprocess
def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' if hostname.startswith('[') else 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in hostname)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if is_safe_hostname(host) and ':' not in host:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error: {e.stderr}'}, 500
    else:
        raise ValueError('Invalid hostname')