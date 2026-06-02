from fastapi import FastAPI
import subprocess
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
class CommandValidator:
    @staticmethod
def validate(host):
        if any(char in host for char in [';', '&', '|', '(', ')']):
            raise ValueError("Invalid characters in hostname")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        validator = CommandValidator()
        validator.validate(host)
        command = ["ping", host]
        response = run_command(command)
        return {"status": "completed", "response": response}
    except ValueError as e:
        return {"error": str(e)}, 400