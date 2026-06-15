from fastapi import FastAPI
import subprocess
class SubprocessWrapper:
    @staticmethod
def run_command(command, args):
        result = subprocess.run([command] + args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    result = SubprocessWrapper.run_command('ping', [host])
    return {"status": "completed", "output": result}