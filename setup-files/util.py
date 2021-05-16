import os
from typing import Dict, List, Tuple
from uuid import uuid4
from collections import defaultdict


def generate_users(num_players: int) -> List[Tuple[str, str]]:
  users: List[Tuple[str, str]] = []

  for _ in range(num_players):
    username = uuid4().hex[:7]
    password = uuid4().hex[:8]
    
    users.append((username, password))
  
  return users

def generate_flags(num_users: int, challenge_names: List[str]):
  flags: Dict[str, List[str]] = defaultdict(list)

  for chal_name in challenge_names:
    for _ in range(num_users):
      flag = f'MACS{{{uuid4().hex}}}'
      flags[chal_name].append(flag)
  
  return flags

def create_user_accounts(users: List[Tuple[str, str]]):
  for username, password in users:
    print(f'Creating user: {username} with password: {password}')
    os.system(f'useradd -m {username} -s /bin/bash')
    os.system(f'echo {username}:{password} | chpasswd')

def save_users(users: List[Tuple[str, str]], flags: Dict[str, List[str]]):
  with open('users.csv', 'w') as f:
    f.write('username, password')

    for k,v in flags.items():
      f.write(f', flag_{k}')
    f.write('\n')

    for i, (username, password) in enumerate(users):
      f.write(f'{username}, {password}, ')

      flagstr = ''
      for k,v in flags.items():
        flagstr += f', {v[i]}'

      f.write(flagstr + '\n')

def special_challenges_setup():
  # Setup for sudo challenge
  os.system('useradd -m -p pleasedonthackme coworker')

  # Setup cronjob for editor challenge
  os.system('chmod +x /root/unlock.sh')
  os.system('echo "*/1 * * * * root /root/unlock.sh" > /etc/cron.d/editor-chal')