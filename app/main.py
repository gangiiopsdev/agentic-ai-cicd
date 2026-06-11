from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize input to prevent command injection
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))
        try:
            output = subprocess.check_output(['ping', sanitized_host], text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}