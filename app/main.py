from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'host': host, 'message': 'Ping successful', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'message': 'Ping failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    if not valid_host(host):
        return {'error': 'Invalid hostname'}
    return ping(host)

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def valid_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts