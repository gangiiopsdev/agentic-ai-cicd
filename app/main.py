from fastapi import FastAPI
import subprocess
class SafeCommandRunner:
    @staticmethod
def run(command: list, input_data=None):
        result = subprocess.run(command, input=input_data, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f'Command failed with return code {result.returncode}: {result.stderr}')

app = FastAPI()

def validate_host(host):
    # Basic validation for host format
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        runner = SafeCommandRunner()
        output = runner.run(['ping', host])
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}