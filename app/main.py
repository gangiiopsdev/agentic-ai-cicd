from fastapi import FastAPI, HTTPException
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> list:
        # Implement proper sanitization logic here
        return shlex.split(command)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_command = CommandSanitizer.sanitize(host)
        result = subprocess.run(['ping'] + [arg for arg in sanitized_command if arg.strip()], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))