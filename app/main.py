from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'localhost']  # Default safe command

    def set_host(self, host):
        self.ping_command[1] = shlex.quote(host)

    def execute(self):
        try:
            output = subprocess.check_output(self.ping_command, stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8'))

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.set_host(host)
    return {'status': safe_ping_instance.execute()}