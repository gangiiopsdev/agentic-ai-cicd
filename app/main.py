from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True).decode('utf-8').strip()], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Host not allowed'}