from fastapi import FastAPI
import subprocess
import ipaddress
def escape_shell_arg(arg):
    """Escape a shell argument by quoting it."""
    return shlex.quote(arg)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
    except ValueError:
        try:
            ipaddress.ip_network(host)
        except ValueError:
            return False
    return True