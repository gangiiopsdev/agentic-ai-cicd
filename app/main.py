from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Regex pattern for a simple hostname or IP address validation
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host parameter')
    # Use a full path for the executable and avoid using input()
    subprocess.run(['/bin/ping', '-c', '1', shlex.quote(host)], check=True)
    return {'status': 'completed'}