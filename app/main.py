from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(user_input):
    # Add your sanitization logic here
    return user_input.strip()

def validate_host(host):
    # Validate the host input to ensure it's a valid hostname or IP address
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        try:
            subprocess.call(shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}'))
        except Exception as e:
            return {'error': str(e)}

        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host input'}