from fastapi import FastAPI
import subprocess
git_command = ['ping', host]
subprocess.call(git_command, shell=False)
return {'status': 'completed'}