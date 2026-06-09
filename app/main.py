from fastapi import FastAPI
import subprocess
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class HostValidator:
    def __init__(self, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._'):
        self.allowed_chars = allowed_chars

    def validate(self, host):
        for char in host:
            if char not in self.allowed_chars:
                raise ValueError(f'Invalid character in host: {char}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validator = HostValidator()
    validator.validate(host)
    safe_command = ['ping', host]
    output = run_safe_command(safe_command)
    return {'status': 'completed', 'output': output}