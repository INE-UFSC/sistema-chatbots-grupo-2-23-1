from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa

        for bot in lista_bots:
            if not isinstance(bot, Bot):
                raise TypeError('Objeto presente na lista de bots não é um bot.')

        self.__lista_bots = lista_bots
        self.__bot = None

    def boas_vindas(self):
        print(f'Saudações, este é o sistema de chatbots integrados da {self.__empresa}.')

    def mostra_menu(self):
        print(f'Os chatbots disponíveis são:')

        for (i, bot) in enumerate(self.__lista_bots):
            print(f'{i} - Bot: {bot.nome} - Apresentação: ', end='')
            bot.apresentacao()

    def escolhe_bot(self):
        escolha = int(input('Digite o número do bot desejado: '))

        if escolha < 0 or escolha > len(self.__lista_bots):
            raise IndexError(f'Bot com número {escolha} não está na lista.')

        self.__bot = self.__lista_bots[escolha] 

    def mostra_comandos_bot(self):

        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        continuar = True
        while continuar:
            self.__bot.mostra_comandos()

            comando_num = int(input('Digite o comando desejado (ou -1 para sair): '))

            if comando_num == -1:
                break

            try:
                print('\n--> ', end='')
                continuar = self.__bot.executa_comando(str(comando_num))
                print()
            except IndexError:
                raise IndexError('Comando não disponível no chatbot.')
        
    
    def inicio(self):
        x = True
        while x:
            self.boas_vindas()

            print()

            self.mostra_menu()

            self.escolhe_bot()

            print('\n--> ', end='')
            self.__bot.boas_vindas()
            print()

            self.le_envia_comando()
            
            while True:
                x = (input("Quer continuar? [Y/N]: ")).lower()
                print()
                if x == "n": 
                    exit()
                elif x != "y": 
                    print("Digite uma forma válida")
                    print()
                else:    
                    self.inicio()
    
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
