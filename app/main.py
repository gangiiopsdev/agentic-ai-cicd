from fastapi import FastAPI
import subprocess
class ShellSafeCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, shell=False, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    try:
        proc = ShellSafeCommand(command)
        proc.wait()
        return {"status": "completed", "exit_code": proc.returncode}
    except Exception as e:
        return {"status": "failed", "error": str(e)}