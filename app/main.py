from fastapi import FastAPI
import subprocess
def safe_ping(command: str) -> bool:
    allowed_commands = {'ping'}
    return command in allowed_commands

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    safe_command = f'ping {host}'
    if safe_ping(safe_command.split()[0]):
        try:
            result = subprocess.run(safe_command, check=True, capture_output=True, text=True)
            return {
                'status': 'completed',
                'output': result.stdout,
                'stderr': result.stderr
            }
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Command not allowed'}