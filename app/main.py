from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, *args, **kwargs)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode('utf-8'))

app = FastAPI()
def safe_ping(host: str):
    # Validate and sanitize input to prevent OS command injection
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid host name")
    command = f'ping {host}'
    return SafeSubprocess.run(command)

@app.get("/ping")
def ping(host: str):
    return safe_ping(shlex.quote(host))