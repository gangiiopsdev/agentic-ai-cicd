from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.post("/ping")
def ping_host(host: str):
    cmd = ['ping', '-c', '1']
    host_parts = host.split()
    for part in host_parts:
        if not part.isnumeric() or len(part) > 15:
            return {'status': 'error', 'message': 'Invalid input'}
        cmd.append(shlex.quote(part))

    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}