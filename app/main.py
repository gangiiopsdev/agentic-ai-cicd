from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.Popen and shell=False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=False)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

def validate_host(host):
    # Validate the host to prevent malicious input
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'stdout': e.stdout.decode(), 'stderr': e.stderr.decode()}
    except ValueError as e:
        return {'error': str(e)}