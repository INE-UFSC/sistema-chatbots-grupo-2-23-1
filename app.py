#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMetrossexual import BotMetrossexual
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotMetrossexual("Ken"), BotTriste("Cleber"), BotFeliz("Reef")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
