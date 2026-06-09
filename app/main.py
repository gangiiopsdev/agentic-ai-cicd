from fastapi import FastAPI
import subprocess
import shlex
class Sanitizer:
    @staticmethod
    def sanitize_input(value: str) -> str:
        return shlex.quote(value)

app = FastAPI()
def safe_ping(host: str):
    try:
        sanitized_host = Sanitizer.sanitize_input(host)
        result = subprocess.run(['ping', '-c', '1'], check=True, capture_output=True, text=True)
        result = result.stdout.replace('\n', '')
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Using a safe wrapper function to handle the ping command.
    return safe_ping(host)