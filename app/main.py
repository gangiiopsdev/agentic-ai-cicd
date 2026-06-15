from fastapi import FastAPI
import subprocess
import shlex
class SanitizedSubprocess:
    @staticmethod
def run_safe_command(command_parts):
        try:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = shlex.quote(host)
    command_parts = ['ping', sanitized_host]
    return SanitizedSubprocess.run_safe_command(command_parts)