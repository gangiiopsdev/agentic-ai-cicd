from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Validate and sanitize the host input before using it in the subprocess call
            if not self.host or not all(c.isalnum() or c in [".", "-"] for c in self.host):
                return {'status': 'error', 'message': 'Invalid host'}

            args = ['ping', '-c', '4'] + [shlex.quote(arg) for arg in shlex.split(self.host)]
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in the subprocess call
    if not host or not all(c.isalnum() or c in [".", "-"] for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()