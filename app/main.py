from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.Popen
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand(host="example.com")

    def ping(self):
        return self.ping_command.execute()

app = FastAPI()

@app.get("/ping")
def ping():
    router = PingRouter()
    result = router.ping()
    return {'status': 'completed', 'result': result}