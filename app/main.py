from fastapi import FastAPI
import subprocess

class PingService:
    def ping(self, host: str):
        # Safer implementation using subprocess.run with proper validation and sanitization
        if not self.is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic for the host parameter
        allowed_hosts = ['example.com', 'localhost']
        return host in allowed_hosts