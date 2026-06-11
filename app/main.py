from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        try:
            result = subprocess.run(command, check=True, capture_output=True, *args, **kwargs)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode())

app = FastAPI()
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_str if char in allowed_chars)

def validate_command(command):
    valid_commands = ['ping', '-c']
    if not all(cmd in valid_commands for cmd in command.split()):
        raise ValueError('Invalid command')

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    command = f'ping -c 1 {safe_host}'
    validate_command(command)
    output = SafeSubprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": output.stdout.decode()}