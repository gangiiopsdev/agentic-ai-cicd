from fastapi import FastAPI
def run_ping(host: str):
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}