from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, capture_output=True, text=True, check=True):
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=capture_output, text=text, check=check)
        return result

app = FastAPI()
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add more hosts as needed
    if host not in allowed_hosts:
        raise ValueError(f'Invalid host: {host}')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        command = f"ping {host}"
        result = SafeSubprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}