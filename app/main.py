from fastapi import FastAPI
def ping(host: str):
    sanitized_host = host.strip().replace(';', '').replace('&', '')
    # Use an alternative for safe execution
    try:
        result = os.system(f'ping -c 1 {sanitized_host}')
        return {'status': 'completed', 'output': result}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)