import random
import string
import os
from uuid import uuid4
from base64 import b64encode

def setup_ls_flag(homedir: str, flag: str):
    # ls flag
    with open(f'{homedir}/{flag}', 'w'):
      pass

def setup_ls_all_flag(homedir: str, flag: str):
  # ls -a flag
  with open(f'{homedir}/.{flag}', 'w'):
    pass

def setup_cat_flag(homedir: str, flag:str):
    with open(f'{homedir}/.read_me!', 'w') as f:
      f.write(f'{flag}\n')

def setup_grep_flag(homedir:str, flag:str):
    alph = string.printable
    for c in string.whitespace:
      alph = alph.replace(c, '')
    s = ''
    for i in range(100000):
      s += random.choice(alph)

    i = random.randint(200, 100000-200)

    s = s[:i] + flag + s[:i]

    os.mkdir(f'{homedir}/.secret')
    with open(f'{homedir}/.secret/search_me!', 'w') as f:
      f.write(s)

def setup_find_flag(homedir: str, flag: str):
    os.mkdir(f'{homedir}/find_me_in_here')
    x, y, z = [random.randint(0, 19)]*3

    for i in range(20):
      try:
        dirname = uuid4().hex[:6]
        os.mkdir(f'{homedir}/find_me_in_here/{dirname}')

        for j in range(20):
          dirname2 = uuid4().hex[:6]
          os.mkdir(f'{homedir}/find_me_in_here/{dirname}/{dirname2}')

          for k in range(20):
            dirname3 = uuid4().hex[:6]
            os.mkdir(f'{homedir}/find_me_in_here/{dirname}/{dirname2}/{dirname3}')

            if i == x and j == y and k == z:
              with open(f'{homedir}/find_me_in_here/{dirname}/{dirname2}/{dirname3}/{uuid4().hex[:6]}', 'w') as f:
                f.write(f'{b64encode(flag.encode()).decode()}\n')
            else:
              with open(f'{homedir}/find_me_in_here/{dirname}/{dirname2}/{dirname3}/{uuid4().hex[:6]}', 'w'):
                pass
      except:
        continue

def setup_sudo_flag(homedir: str, flag: str, username: str):
    # Have permission to use cat as another user using the sudo command
    # NOTE: Setup for sudo is earlier.
    lines = []
    with open('/etc/sudoers', 'r') as f:
      lines = f.readlines()

    with open('/etc/sudoers', 'w') as f:
      lines = lines[:-1] + [f"{username} ALL=(coworker) NOPASSWD:/usr/bin/cat\n"] + lines[-1:]
      f.writelines(lines)

    challenge_dir = f'{homedir}/super_execution'
    os.mkdir(challenge_dir)

    # Create flag file only readable by coworker
    with open(f'{challenge_dir}/flag.txt', 'w') as f:
      f.write(f'{flag}\n')
    os.system(f'chown coworker:coworker {challenge_dir}/flag.txt')
    os.system(f'chmod 400 {challenge_dir}/flag.txt')

def setup_exec_file_flag(homedir: str, flag: str):
    challenge_dir = f'{homedir}/execution'
    os.mkdir(challenge_dir)

    # Compile readFlag program into folder and make into suid
    os.system(f'gcc ./readFlag.c -o {challenge_dir}/readFlag')
    os.system(f'sudo chown root:root {challenge_dir}/readFlag')
    os.system(f'sudo chmod 4555 {challenge_dir}/readFlag')

    # Create flag file only readable by root
    with open(f'{challenge_dir}/flag.txt', 'w') as f:
      f.write(f'{flag}\n')
    # Should be already owned by root
    os.system(f'chmod 400 {challenge_dir}/flag.txt')

def setup_editor_flag(homedir: str, flag: str):
    # Cronjob will be set to look at the options.txt and see if show_flag is set to True
    # NOTE: Cronjob is setup earlier.
    challenge_dir = f'{homedir}/editor'
    os.mkdir(challenge_dir)

    # Create flag file only readable by root
    with open(f'{challenge_dir}/flag.txt', 'w') as f:
      f.write(f'{flag}\n')
    # Should be already owned by root
    os.system(f'chmod 400 {challenge_dir}/flag.txt')

    with open(f'{challenge_dir}/options.txt', 'w') as f:
      f.write("unlock_flag=False\n")
    # Allow them to edit the file
    os.system(f'chmod 666 {challenge_dir}/options.txt')
