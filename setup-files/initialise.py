from typing import Dict, List, Tuple
from collections import defaultdict
from uuid import uuid4
import os

from flags import *
from util import *
from ctfd_util import add_challenges_to_ctfd

CHALLENGE_NAMES = ['ls', 'ls_all', 'cat', 'grep', 'find', 'exec', 'sudo', 'editor']
NUM_PLAYERS = int(os.environ.get("NUM_PLAYERS", 5))

def main():
  # List of username and password pairs
  users: List[Tuple[str, str]] = generate_users(NUM_PLAYERS)

  # Generate unique flags per user per challenge
  # Mapping from challenge name to list of flags
  flags: Dict[str, List[str]] = generate_flags(NUM_PLAYERS, CHALLENGE_NAMES)

  # Create user accounts and home dirs
  create_user_accounts(users)

  # Save the usernames and passwords in a csv
  save_users(users, flags)

  # setup things like extra users, cron jobs...
  special_challenges_setup()

  # Put the flags in their places
  for i, (username, _) in enumerate(users):
    homedir = f'/home/{username}'

    setup_ls_flag(homedir, flags['ls'][i])
    setup_ls_all_flag(homedir, flags['ls_all'][i])
    setup_cat_flag(homedir, flags['cat'][i])
    setup_grep_flag(homedir, flags['grep'][i])
    setup_find_flag(homedir, flags['find'][i])
    setup_exec_file_flag(homedir, flags['exec'][i])
    setup_sudo_flag(homedir, flags['sudo'][i], username)
    setup_editor_flag(homedir, flags['editor'][i])
  
  CTFD_API_KEY = os.environ['CTFD_API_KEY']
  if CTFD_API_KEY:
    add_challenges_to_ctfd(flags, 'https://ctfd.macs.codes', CTFD_API_KEY)

if __name__ == '__main__':
  main()
