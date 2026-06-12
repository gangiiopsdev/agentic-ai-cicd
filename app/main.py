from fastapi import FastAPI, HTTPException
import re
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> list:
        # Implement proper sanitization logic here
        sanitized_args = [arg.strip() for arg in command.split() if re.match(r'^[a-zA-Z0-9]+$', arg)]
        return sanitized_args or ['echo', 'InvalidArgument']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not re.match(r'^[a-zA-Z0-9]+$', host):
            raise HTTPException(status_code=400, detail='Invalid host format')
        sanitized_host = CommandSanitizer.sanitize(host)
        result = subprocess.run(['ping'] + sanitized_host, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))