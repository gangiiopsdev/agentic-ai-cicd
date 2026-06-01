from fastapi import FastAPI
import shlex
import re
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
def validate_host(host):
    # Basic regex to allow only valid hostname characters and some common special characters
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = shlex.quote(host)
        result = subprocess.run(shlex.split(f"ping {sanitized_host}"), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}