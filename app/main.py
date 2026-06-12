from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400

    # Use shlex.quote to safely escape command arguments
    from shlex import quote
    safe_host = quote(host)
    ping_command = subprocess.Popen(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ping_command.communicate()
    return {'status': 'completed', 'output': stdout.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)