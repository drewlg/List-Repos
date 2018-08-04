# List-Repos
Simple program that lists USER_NAME Github public repositories.

## Instructions:
1. Download ListRepos.py file to local computer. 
2. Open the terminal and navigate to the directory the file was cloned into (`cd [path]`).
3. Run:
    - To deploy `python ListRepos.py`  
        or `python ListRepos.py --user_name [USER_NAME]`
    - For Help `python ListRepos.py --h`
   
### Help:
```bash
      Usage: ListRepos.py [OPTIONS]

      Simple program that lists USER_NAME Github repositories.

      Options:
        --user_name TEXT  Github Username. Example:PyAntony.
        --help            Show this message and exit.
```

### Dependencies:

   - Language:  
      - Python 3.6  
   - Requests:  
      - run `pip install requests`  
   - Click:  
      - run `pip install click`
