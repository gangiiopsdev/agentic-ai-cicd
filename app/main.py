from fastapi import FastAPI
import subprocess
git_command = f"ping {host}"
# Remove the shell=True parameter to mitigate the risk of command injection
subprocess.run(git_command, check=True, shell=False)
return {'status': 'completed'}