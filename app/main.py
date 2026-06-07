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
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Using a safe wrapper function to handle the ping command.
    return safe_ping(host)