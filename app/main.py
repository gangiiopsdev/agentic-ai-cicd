from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

    async def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = SafeSubprocess(host)
    return await safe_host.execute()