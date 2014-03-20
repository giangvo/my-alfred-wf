
import alfred
import os
import sys
import re

URL_PATTERN = "url = git@([^:]+):(.*)/(.*)\.git"
HOME = os.environ['HOME']
CONF_PLUGINS_DIR = HOME + '/codes/conf/plugins/'
#get plugin query name
query = sys.argv[1].strip() if len(sys.argv) > 1 else ""

# Get plugin repo url
def get_git_info(dir):
    url = ""
    fullPath = dir + "/.git/config"
    if os.path.exists(fullPath):
        lines = open(fullPath)
        for line in lines:
            line = line.strip()
            pattern = re.compile(URL_PATTERN)
            m = pattern.match(line)
            if m:
                url = "https://" + m.group(1) + "/" + m.group(2) + "/" + m.group(3)
                break
    else:
        url = "Not a git repo"
    return url
    
###
feedback = alfred.Feedback()
for dir_name in os.listdir(CONF_PLUGINS_DIR):
    if query and not query in dir_name:
        continue
    fullPath = os.path.join(CONF_PLUGINS_DIR, dir_name)

    if os.path.isdir(fullPath):
        url = get_git_info(fullPath)
        if not url:
            continue
        feedback.addItem(title=dir_name
            , subtitle=fullPath.replace(HOME,"~") + "  |  " + url
            , arg=fullPath + "|" + url
            , icon='icon.png'
            , valid=True)
feedback.output()


