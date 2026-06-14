from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['127.0.0.1', 'localhost']:
        command = ['ping', host]
        for arg in command:
            if not isinstance(arg, str) or '&&' in arg or '|' in arg or ';' in arg or '`' in arg:
                raise ValueError('Invalid command argument')
        result = subprocess.run(command, check=True, capture_output=True)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)