from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use subprocess.run with a list to avoid shell injection
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize the host input to prevent command execution
            sanitized_host = ''.join(filter(str.isalnum, host))
            ping_command = PingCommand(sanitized_host)
            output = ping_command.execute()
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}