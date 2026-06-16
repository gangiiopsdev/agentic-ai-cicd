from fastapi import FastAPI
import subprocess
class SubprocessWrapper:
    @staticmethod
def run_command(command, args):
        result = subprocess.run([command] + [arg for arg in args if isinstance(arg, str)], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):\n    if not validate_host(host):\n        raise ValueError("Invalid host")\n    result = SubprocessWrapper.run_command('ping', [host])\n    return {"status": "completed", "output": result}