from fastapi import FastAPI
import subprocess
import shlex
class FastAPISubprocess:
    def call(self, cmd):
        try:
            result = subprocess.run(cmd, shell=False, capture_output=True, text=True)
            return result.stdout, result.stderr
        except Exception as e:
            return None, str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = ''.join(e for e in host if e.isalnum() or e.isdigit())
    cmd = shlex.split(f"ping {sanitized_host}")
    return FastAPISubprocess().call(cmd)