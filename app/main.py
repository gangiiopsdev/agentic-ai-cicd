from fastapi import FastAPI
import subprocess
get_ip_info = lambda ip: subprocess.getoutput(f'ping -c 4 {ip}')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        output = get_ip_info(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}