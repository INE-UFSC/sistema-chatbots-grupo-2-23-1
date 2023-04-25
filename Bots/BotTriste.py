from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self):
        self.__nome = "Cleber"

    def apresentacao(self):
        print(f"Sniff. Meu nome é {self.__nome} e tenho tristeza crônica.")
    
    def mostra_comandos(self):
        print("1 - Bom dia!!!")
        print("2 - Qual o seu nome queridissimo ?")
        print("3 - Qual seu conhecimento desbalanceado ?")
        print("4 - Sua tristeza é irradiante. Adeus!")
    
    def executa_comando(self,cmd):
        if cmd == "1":
            print(" Sniff. Porque você esta tão feliz em uma terça feira de manhã ?")
        elif cmd == "2":
            print(f" Talvez você não tenha escutado porque não falo alto por causa da ansiedade social, mas meu nome é {self.__nome}")
        elif cmd == "3":
            print("A solidão é, antes de mais nada, restauradora. Um descanso da vida social, dos deveres sociais, das máscaras que vestimos tantas vezes em público. Ela é necessária, para revigorar, repousar. \
                 Roubei essa frase de Nietzsche para parecer inteligente, mas meu conhecimento é pífio que nem minha vida.")
        elif cmd == "4":
            BotTriste.despedida()
    
    def boas_vindas(self):
        print("Fico tão contente que você me escolheu, finalmente vou falar com alguém!")

    def despedida(self):
        print("Não me deixe sozinho por favor!!!")