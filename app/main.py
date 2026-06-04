from fastapi import FastAPI
import subprocess
class PingCommandValidator:
    @staticmethod
def is_valid_command(command: str) -> bool:
        allowed_commands = ['ping']
        return command in allowed_commands

app = FastAPI()

def ping(host: str):
    if not PingCommandValidator.is_valid_command('ping'):
        raise ValueError('Invalid command')
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)