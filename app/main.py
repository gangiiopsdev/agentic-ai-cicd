from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', shlex.quote(self.host)], stderr=subprocess.STDOUT)
            return output.decode('utf-8'), None
        except subprocess.CalledProcessError as e:
            return str(e), e.returncode

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result, error_code = ping_command.execute()
    if error_code is not None:
        return {"status": "failed", "error": result}
    else:
        return {"status": "completed", "result": result}