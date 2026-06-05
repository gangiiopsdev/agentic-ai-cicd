from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        generate_ping_command = subprocess.run(['ping', host], capture_output=True, text=True)
        return generate_ping_command.stdout
    else:
        return {'error': 'Invalid host'}