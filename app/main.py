from fastapi import FastAPI
import subprocess
class PingCommandRunner:
    def run(self, host: str):
        # Secure implementation
        args = ['ping', host]
        subprocess.run(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    runner = PingCommandRunner()
    runner.run(host)
    return {"status": "completed"}