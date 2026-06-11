from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(input_str):
        return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    try:
        output = subprocess.run(['ping', '--{}'.format(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}