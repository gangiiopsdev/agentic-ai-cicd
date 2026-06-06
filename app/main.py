from fastapi import FastAPI
import subprocess
import shlex
class SanitizedSubprocess:
    @staticmethod
def run(command):
        if isinstance(command, str):
            command = shlex.split(command)
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.stdout

app = FastAPI()

def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    try:
        response = SanitizedSubprocess.run(['ping', '-c', '1', sanitized_host])
        return {'status': 'completed', 'response': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}