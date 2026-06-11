from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        sanitized_command = [subprocess.quote(arg) for arg in command]
        return subprocess.run(sanitized_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = SafeSubprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}