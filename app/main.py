from fastapi import FastAPI
import subprocess
import shlex

global ALLOWED_HOSTS = ['example.com', 'test.example.com']  # Define a list of allowed hosts

app = FastAPI()

def validate_host(host: str):
    return host in ALLOWED_HOSTS

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        ping_command = shlex.split(f"ping {host}")
        generate_ping_command = subprocess.run(ping_command, capture_output=True, text=True)
        return generate_ping_command.stdout
    else:
        return {'error': 'Invalid host'}