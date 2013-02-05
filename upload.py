import os

cmd_1 = "git add ."
cmd_2 = 'git commit -m "new_log"'
cmd_3 = 'git push origin gh-pages'

os.system(cmd_1)
os.system(cmd_2)
os.system(cmd_3)
