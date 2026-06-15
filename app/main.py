from fastapi import FastAPI
import subprocess
class SafeCommandRunner:
    @staticmethod
def run_command(command: str, args: list):
        try:
            output = subprocess.check_output([command] + args, stderr=subprocess.STDOUT, text=True)
            return {"status": "completed", "output": output}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_runner = SafeCommandRunner()
    return safe_runner.run_command("ping", [host])