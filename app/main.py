from fastapi import FastAPI
import subprocess
import shlex
cimport re

app = FastAPI()

def sanitize_input(input_str):
    # Complex sanitization using regular expression to allow only alphanumeric characters and periods, and escape special shell characters
    sanitized = re.sub(r'[^a-zA-Z0-9.\^$*+?(){}|:<>~`]', '', input_str)
    return shlex.quote(sanitized)

def validate_host(host):
    # Validate the host format to ensure it's safe for ping command
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        raise ValueError('Invalid IP address')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        args = shlex.split('ping') + [host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}