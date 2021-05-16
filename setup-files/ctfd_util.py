import subprocess
import glob
from typing import Dict, List
from jinja2 import Environment, FileSystemLoader

def add_challenges_to_ctfd(flags: Dict[str, List[str]], host: str, api_key: str):
  generate_challenge_templates(flags)


  file_loader = FileSystemLoader('./ctfd/templates')
  env = Environment(loader=file_loader)
  template = env.get_template('ctfcli-config')

  output = template.render(url = host, api_key = api_key)

  subprocess.call(['mkdir', '.ctf'])
  with open(f'./.ctf/config', 'w') as f:
    f.write(output)

  for chal_dir in glob.glob('./ctfd/challenges/*'):
    subprocess.call(['ctf', 'challenge', 'install', chal_dir])
  

def generate_challenge_templates(flags: Dict[str, List[str]]):
  file_loader = FileSystemLoader('./ctfd/templates')
  env = Environment(loader=file_loader)

  template = env.get_template('challenge-template.yml')

  for chal_name, chal_flags in flags.items(): 
    output = template.render(challenge_name = chal_name, challenge_flags = chal_flags)

    subprocess.call(['mkdir', '-p', f'./ctfd/challenges/{chal_name}'])
    with open(f'./ctfd/challenges/{chal_name}/challenge.yml', 'w') as f:
      f.write(output)