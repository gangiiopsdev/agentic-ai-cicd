from fastapi import FastAPI
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', '-c', '4', host], check=True)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'success', 'message': f'Ping to {host} successful'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}