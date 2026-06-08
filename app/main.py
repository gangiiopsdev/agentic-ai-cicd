from fastapi import FastAPI, HTTPException
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> list:
        # Implement proper sanitization logic here
        return [arg for arg in command.split() if arg.isalnum()] or ['echo', 'InvalidArgument']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = CommandSanitizer.sanitize(host)
        result = subprocess.run(['ping'] + [arg.strip() for arg in sanitized_host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))