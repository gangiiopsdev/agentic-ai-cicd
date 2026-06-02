from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
def validate_host(host):
    try:
        # Check if the host is a valid IP address or domain name
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):  
    if not validate_host(host):
        return {"status": "invalid host"}
    sanitized_host = sanitize_input(host)
    command = shlex.split(f"ping {sanitized_host}")
    subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
    return {"status": "completed"}