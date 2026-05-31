from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isdigit() and len(char) <= 15)

def safe_ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isdigit() or len(sanitized_host) > 15:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        subprocess.run(['ping', '-c', '4', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400
    except Exception as e:
        return {'error': str(e)}, 500