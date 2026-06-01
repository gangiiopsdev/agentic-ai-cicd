from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate host input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

# Function to validate host input
def is_valid_host(host):\n    # Add validation logic here (e.g., regex match, IP address check)\n    import re\n    pattern = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])$'\n    return re.match(pattern, host) is not None