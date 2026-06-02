from fastapi import FastAPI
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        try:
            args = ['ping', self.host]
            result = Popen(args, stdout=PIPE, stderr=PIPE)
            stdout, stderr = result.communicate()
            return {
                "status": "completed",
                "output": stdout.decode('utf-8')
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "failed"
            }

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.run()