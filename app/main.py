from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement hostname validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stdout': e.stdout.decode(), 'stderr': e.stderr.decode()}
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

# Preventive controls:
# 1. Implement strict hostname validation logic in the is_safe_hostname function.
# 2. Avoid using shlex.split for command arguments if possible.
# 3. Consider using a safer method to execute commands, such as using parameterized queries or an API client.