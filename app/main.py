from fastapi import FastAPI
def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    subprocess.run(['/bin/ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}