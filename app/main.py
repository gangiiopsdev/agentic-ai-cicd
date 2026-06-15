from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        # Validate and sanitize input
        if not self.is_valid_host(host):
            return {'status': 'error', 'message': 'Invalid host'}
        command = ['ping', shlex.quote(host)]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed'}
    def is_valid_host(self, host: str):
        # Simple validation logic
        allowed_hosts = ['example.com', 'test.com']
        return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)