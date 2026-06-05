from fastapi import FastAPI
import subprocess
class SafePinger:
    def ping(self, host):
        try:
            # Validate and sanitize the host input
            if not self.is_valid_host(host):
                return {'status': 'failed', 'error': 'Invalid host'}
            output = subprocess.check_output(['ping', '-c', '1', f'{host}'], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

    def is_valid_host(self, host):
        # Implement validation logic here
        return host.strip().isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    return pinger.ping(host)}