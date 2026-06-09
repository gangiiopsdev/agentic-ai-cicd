from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            # Validate the host to prevent command injection
            if not all(c.isalnum() or c in ['.', '-'] for c in host): raise ValueError('Invalid host name')
            output = subprocess.run(['ping', '-c', '4', '--'], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        except ValueError as ve:
            return {'status': 'failed', 'error': str(ve)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(f'--{host}')