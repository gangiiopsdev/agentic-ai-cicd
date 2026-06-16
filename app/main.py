from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = await subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not self.is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    ping_command = PingCommand(host)
    return ping_command.run()

PingCommand.prototype.is_safe_host = function(host) {
    // Implement logic to check if the host is safe
}