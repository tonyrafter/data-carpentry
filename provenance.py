"""
A collection of commonly used functions for data provenance
"""

import sys
import datetime
import git
import os

def get_history_record(repo_dir):
    """Create a new history record"""
    
    time_stamp = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    exe = sys.executable
    args = " ".join(sys.argv)
    git_hash = git.Repo(repo_dir).heads[0].commit
    
    entry = """%s: %s %s (Git hash: %s)""" %(time_stamp, exe, args, str(git_hash)[0:7])
    
    return entry

