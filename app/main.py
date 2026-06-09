from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host argument
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode("utf-8")}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host parameter'}
    return safe_ping(host)