from fastapi import FastAPI
import subprocess
class SafePing:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_ping = SafePing()
    return safe_ping.ping(host)

def is_safe_host(host: str):
    # Implement logic to validate the host, e.g., allow only specific domain names or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts