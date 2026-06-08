from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list, **kwargs):
        try:
            return subprocess.run(command, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f'Command failed with return code {e.returncode}: {e.stderr}')

app = FastAPI()
def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

def sanitize_input(input_data):
    return ''.join(e for e in input_data if e.isalnum() or e in '.-:/' )

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        result = SafeSubprocess.run(['ping', sanitized_host])
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}