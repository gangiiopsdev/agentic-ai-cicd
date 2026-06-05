from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host) and len(host) <= 255
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        if not isinstance(command, list):
            command = shlex.split(command)
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, *args, **kwargs)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return e.stderr.decode() + ' - Command: ' + ' '.join(command)
class SafePing:
    @staticmethod
def ping(host):
        if not validate_host(host):
            raise ValueError('Invalid host')
        command = ['ping', host]
        output = SafeSubprocess.safe_run(command)
        return {"status": "completed", "output": output}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = SafePing.ping(host)
        return result
    except ValueError as e:
        return {"status": "failed", "error": str(e)}