from Bots.Bot import Bot


class BotDramatico(Bot):
    def __init__(self,nome):
        super().__init__(nome)

    def apresentacao(self):
        print(f"Oi... Meu nome é {self._nome}. Como posso te ajudar? Não consigo te ajudar. O que queres de mim?")
    
    def mostra_comandos(self):
        print("1 - Bom dia")
        print("2 - Qual o seu nome ?")
        print("3 - Qual seu conhecimento desbalanceado ?")
        print("4 - Seus músculos são irradiantes. Vou pra academia, adeus!")
    
    def executa_comando(self,cmd):
        if cmd == "1":
            print("")
            print("--> Nunca será um bom dia...")
            print("")
        elif cmd == "2":
            print("")
            print(f"--> Eu já te disse meu nome, é {self._nome}, você já esqueceu de mim?")
            print("")
        elif cmd == "3":
            print("")
            print("--> Desista, o mundo vai acabar mesmo, nada vale a pena...")
            print("")
        elif cmd == "4":
            self.despedida()
            return False
        return True
    
    def boas_vindas(self):
        print("")
        print("--> Por que você me escolheu? Eu não sirvo pra nada, faço tudo errado...")
        print("")

    def despedida(self):
        print("")
        print("--> Você já vai? Não precisa mais de mim? Então, até...")
        print("")
