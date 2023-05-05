from Bots.Bot import Bot
from SistemaChatBot.load_json import load_bot_cmds


class BotImpl(Bot):
    def __init__(self,nome, nome_bot):
        super().__init__(nome)

        self.cmds = load_bot_cmds(nome_bot)

    def apresentacao(self):
        return self.cmds['apresentacao']['msg']

    def mostra_comandos(self):
        for cmd in self.cmds:
            prompt = self.cmds[cmd]['prompt']

            if prompt == None:
                continue

            print(f'{cmd} - {prompt}')

    def executa_comando(self,cmd):
        return self.cmds[cmd]
    
    def boas_vindas(self):
        return self.cmds['boas_vindas']['msg']

    def despedida(self):
        # ARRUMAR
        return self.cmds['4']['msg']