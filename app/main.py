from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command):
    return subprocess.run(command, capture_output=True, text=True, timeout=5)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it's a valid hostname or IP address
        import socket
        socket.inet_pton(socket.AF_INET, host)
        safe_host = shlex.quote(host)
        command = ['ping', safe_host]
        result = safe_subprocess(command)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, socket.error) as e:
        return {'status': 'failed', 'error': str(e)}