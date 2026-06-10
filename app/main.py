from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            response = subprocess.run(['ping', '-c', '4', self.host], check=True, stdout=subprocess.PIPE)
            return True, response.stdout.decode()
        except subprocess.CalledProcessError as e:
            return False, str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'completed', 'success': False, 'message': 'Invalid host'}
    command = PingCommand(host)
    success, message = command.execute()
    return {'status': 'completed', 'success': success, 'message': message}