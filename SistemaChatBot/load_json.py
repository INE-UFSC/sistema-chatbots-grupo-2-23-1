import json

def load_bot_cmds(bot_name):
    f = open(f'./cmds/{bot_name}.json')

    cmds = json.load(f)

    return cmds

load_bot_cmds('metrossexual')