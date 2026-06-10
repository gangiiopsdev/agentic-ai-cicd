from fastapi import FastAPI
import subprocess
generate_safe_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    parsed_host = urlparse(host)
    if not parsed_host.hostname:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(generate_safe_command(parsed_host.hostname), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}