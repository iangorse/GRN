from templite import Templite
import subprocess
import argparse
import os
import sys

def parseArguments():
    ''' Parse the command line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument("template", help="the template file to use")
    parser.add_argument("--gitdir", help="the git repository path to build release notes against")
    parser.add_argument("--output", help="outputs results to a filename")
    args = parser.parse_args()    
    return args

def ExcuteGitLog(git_args):
    ''' Execute the git log command'''
    logs = subprocess.run(git_args, stdout=subprocess.PIPE).stdout.decode('utf-8')
    if logs[:6] == "fatal:" or logs == '':
        print(logs)
        exit(1)
    return logs

def ParseLogs(logs):
    ''' Parses the git log, storing results into a list '''
    commits = []

    for result in logs.split('\n'):
        commit_data = result.split(';')
        date_data = commit_data[2].split(' ')

        commit_hash = commit_data[0]
        commit_author = commit_data[1]
        commit_date = date_data[1] + " " + date_data[2] + " " + date_data[4]
        commit_message = result[result.find(' : ')+3:]   
         
        commit = {}
        commit["hash"] = commit_hash
        commit["date"] = commit_date
        commit["message"] = commit_message
        commit["author"] = commit_author
                
        commits.append(commit) 
    return commits 

def GetTemplate(template):
    ''' Open the template file '''

    # ENSURE THE TEMPLATE FILE EXISTS BEFORE CONTINUING
    template_path = os.path.join("templates", template + ".txt")
    if os.path.exists(template_path) == False:
        print("ERROR: Cannot find template " + template_path + " Please ensure you have used the correct template file")
        sys.exit(1)

    # OPEN THE TEMPLATE DOCUMENT
    content = ""
    with open(template_path, "r") as file:
        content = file.read()
    return content        

if __name__ == "__main__":
    git_args = ['git', 'log', '--pretty=format:%h;%an;%cd : %s']

    args = parseArguments()
    if args.gitdir:
        git_args.insert(1, '--git-dir')
        git_args.insert(2, args.gitdir)

    logs = ExcuteGitLog(git_args)
    commits = ParseLogs(logs)
    content = GetTemplate(args.template)

    t = Templite(content)
    result = t(commitlist=commits)
    print(result)

    if args.output:
        with open(args.output, "wb") as f:
            f.write(result.encode("utf-8"))
    