from fastapi import FastAPI
import subprocess
class PingHandler:
    @staticmethod
def ping(host: str):
        # Sanitize the input to prevent command injection
        safe_host = ''.join(c for c in host if c.isalnum() or c in ['.', '-', '_'])
        try:
            output = subprocess.run(['ping', '--ipv4', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    handler = PingHandler()
    return handler.ping(host)