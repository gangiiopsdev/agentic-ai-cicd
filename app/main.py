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

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = SafeSubprocess.run(['ping', host])
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}