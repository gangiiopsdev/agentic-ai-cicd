from fastapi import FastAPI
import subprocess
import re
class SafePing:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self) -> bool:
        if not self.host or ' ' in self.host:
            return False
        return True

    def run_command(self) -> tuple:
        args = ['ping', '-c', '4', self.host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, result.stdout.decode(), result.stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):      
    safe_ping_instance = SafePing(host)
    if not safe_ping_instance.validate_host():
        return {'error': 'Invalid input'}
    status, output = safe_ping_instance.run_command()    
    if status:
        return {'status': 'completed', 'output': output}
    else:
        return {'error': 'Invalid input'}