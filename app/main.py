from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
global_host = 'example.com'  # Define a global safe default value for host

app = FastAPI()

@app.get("/ping")
def ping(host: str = global_host):  # Use the global safe default value for host
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = PingCommand(host).execute()
    return {'status': 'completed', 'result': result}
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex to check if the host is valid
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None