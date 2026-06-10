from fastapi import FastAPI
import subprocess
class SanitizedCommandRunner:
    def __init__(self):
        self.allowed_commands = ['ping']

    def run_command(self, args):
        if args[0] not in self.allowed_commands:
            raise ValueError('Invalid command')
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode('utf-8'), error.decode('utf-8')

app = FastAPI()
token_auth_scheme = HTTPBearer()
sanitized_runner = SanitizedCommandRunner()
def run_command(args):
    return sanitized_runner.run_command(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str, token: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    if not is_valid_token(token.credentials):
        return HTTPException(status_code=403, detail="Invalid token")
    args = ["ping", host]
    output, error = run_command(args)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}
def is_valid_token(token: str):
    # Add your token validation logic here
    pass