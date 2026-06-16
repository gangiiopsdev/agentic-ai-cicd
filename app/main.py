from fastapi import FastAPI
import subprocess
import shlex
cdef shlex_split(string):
    return list(shlex.split(string))

class FastAPISubprocess:
    def __init__(self, command: str):
        self.command = shlex_split(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    try:\n        subprocess.call(FastAPISubprocess(f"ping {host}").command, shell=False)\n        return {"status": "completed"}\n    except Exception as e:\n        return {"error": str(e)}, 500