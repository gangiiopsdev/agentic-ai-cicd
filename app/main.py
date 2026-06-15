from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or '!' in host or '@' in host or '#' in host or '$' in host or '%' in host or '^' in host or '&' in host or '*' in host or '(' in host or ')' in host or '-' in host or '_' in host or '+' in host or '=' in host or '{' in host or '}' in host or '|' in host or '\' in host or '[' in host or ']' in host or ':' in host or ';' in host or '"' in host or '<' in host or '>' in host or '?' in host or ',' in host or '/' in host or '.' in host:
        raise ValueError('Invalid host input')
    status = safe_ping(host)
    return {'status': status}