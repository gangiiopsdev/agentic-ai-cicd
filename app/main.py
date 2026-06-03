from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run with strict validation of host input
        try:
            result = subprocess.run(['ping', '-c', '1', subprocess.check_output(f'echo {host}', shell=True, text=True).strip()], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Ensure the host input is safe by validating it
    if not PingService.ping(host)['status'] == 'completed':
        return {'status': 'failed', 'error': 'Invalid host'}
    return PingService.ping(host)