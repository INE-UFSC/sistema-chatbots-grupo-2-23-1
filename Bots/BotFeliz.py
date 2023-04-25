from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)

    def apresentacao(self):
        print("Olá, sou o Reef e te amo!!!")

    @nome.setter
    def nome(self, nome):
        super.nome(nome)

    @property
    def nome(self):
        super.nome()

    def mostra_comandos(self):
        print("1 - Boas vindas.")
        print("2 - Qual o seu nome?")
        print("3 - Quero um conselho.")
        print("4 - Adeus.")
        
    
    def executa_comando(self,cmd):
        if cmd == 1:
            print("Como posso ajudá-lo?")
        elif cmd == 2:
            print("Meu nome é Reef.")
        elif cmd == 3:
            print("Não tenha medo de ser você mesmo e vá em busca dos seus sonhos.")
        elif cmd == 4:
            print("Tchau e até a próxima.")
            
    def boas_vindas(self):
        print("- - > Reef diz: Olá, pessoa maravilhosa. Estou muito feliz que você me escolheu.")

    def despedida(self):
        print("- - > Reef diz: Foi um prazer ajudar")