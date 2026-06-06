from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Use a whitelist of allowed hosts or validate the host input
            if host not in ['127.0.0.1', '::1']:  # Example whitelist
                return {'status': 'failed', 'error': 'Invalid host'}
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}