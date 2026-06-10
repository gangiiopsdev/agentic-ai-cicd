from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

def execute_ping(host):
    try:
        # Sanitize the host input to prevent command execution
        sanitized_host = ''.join(filter(str.isalnum, host.replace('.', '')))  # Allow only alphanumeric characters and dots
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
class PingEndpoint:
    @staticmethod
    def ping(host: str):
        return execute_ping(host)