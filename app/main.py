from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str):
        super().__init__(['ping', subprocess.list2cmdline(host.split())], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        process = PingCommand(host)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}