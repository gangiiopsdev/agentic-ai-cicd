from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Validate the host input to ensure it's safe
            if not self.is_valid_host(host):
                return {'status': 'failed', 'error': 'Invalid host'}
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

    def is_valid_host(self, host: str) -> bool:
        # Implement validation logic here (e.g., regex matching allowed characters)
        import re
        pattern = r'^[a-zA-Z0-9.-]+$'
        return re.match(pattern, host) is not None