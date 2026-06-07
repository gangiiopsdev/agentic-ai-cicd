from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    host_parts = host.split()
    return all(part.isnumeric() and len(part) <= 15 for part in host_parts)

app = FastAPI()

@app.post("/ping")
def ping_host(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    cmd = ['ping', '-c', '1']
    host_parts = host.split()
    for part in host_parts:
        cmd.append(shlex.quote(part))

    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}