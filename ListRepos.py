
import requests as rq
import click

@click.command()
@click.option('--user_name', prompt='\nEnter Github user name (developer name:PyAntony)', 
              help='Github Username. Example:PyAntony')


def main(user_name):
    
    """Simple program that lists USER_NAME Github repositories."""
    
    num = 0
    repo_list = list()

    # Loop for pagination: iterate over every page and store repository names
    while True: 
    
        GitURL = 'https://api.github.com/users/{}/repos?page={}'.format(user_name, num)
        r = rq.get(GitURL)
        
        try:
            repo_list = repo_list + [dc['name'] for dc in r.json()] 
        except:
            # API daily limit exceeded 
            print('\n', r, '\n', r.json()['message'])
            exit()
            break
    
        if len(r.json()) == 0:
            break
    
        num += 1
  
    repo_num = len(set(repo_list))
    click.echo('Number of repos: {}\n'.format(repo_num))

    for repo in set(repo_list):
        click.echo(repo)

if __name__ == '__main__':
    main()
        

