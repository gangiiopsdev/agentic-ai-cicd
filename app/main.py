from fastapi import FastAPI
import subprocess

def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "anotherdomain.com"]
    return host in allowed_hosts

class SafeHostsException(Exception):
    pass

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")

    try:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise SafeHostsException(f"Failed to ping {host}: {e.stderr}") from e