from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        if not all(c.isalnum() or c in '.:-' for c in host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}