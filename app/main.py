from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def run_command(self, host: str, cmd_template: str) -> dict:
        if host not in self.allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            # Sanitize the command template and input
            sanitized_cmd_template = shlex.quote(cmd_template)
            cmd = shlex.split(sanitized_cmd_template.format(host=host))
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
safe_runner = SafeCommandRunner(allowed_hosts=['example.com', 'localhost'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_runner.run_command(host, 'ping {host}')