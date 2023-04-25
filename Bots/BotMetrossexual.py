from Bots.Bot import Bot

class BotMetrossexual(Bot):
    def __init__(self,nome):
        super().__init__(nome)

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(self,nome):
        super().nome(nome)

    def apresentacao(self):
        print(f"Toma do double biceps do pai, pode me chamar de {self.__nome}, mas você tchutchuca, pode me chamar todo dia.")
    
    def mostra_comandos(self):
        print("1 - Bom dia")
        print("2 - Qual o seu nome ?")
        print("3 - Qual seu conhecimento desbalanceado ?")
        print("4 - Seus músculos são irradiantes. Vou pra academia, adeus!")
    
    def executa_comando(self,cmd):
        if cmd == "1":
            print("Bom dia pra ken ??? Hahahaha, te peguei.")
        elif cmd == "2":
            print(f"Metrossexual de plástico, ou {self.__nome}, ás vezes amor da sua vida.")
        elif cmd == "3":
            print("Tome 1 grama de whey protein por kilo de massa corporal. Me agradeça depois.")
        elif cmd == "4":
            BotMetrossexual.despedida()
    
    def boas_vindas(self):
        print("Tá saindo da jaula o monstro!")

    def despedida(self):
        print("Pode ir, sei que vai voltar. BIRL!")