from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input using regex or similar method
            sanitized_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_', ' ', ':'])
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}