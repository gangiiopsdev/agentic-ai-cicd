from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    if 'localhost' in host:
        return f'ping {host}'
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):    
    try:
        command = generate_ping_command(host)
        subprocess.run(command.split(), shell=False, check=True, capture_output=True)
        return {'status': 'completed', 'output': command.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}