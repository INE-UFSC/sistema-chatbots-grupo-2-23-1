#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from Bots.BotMetrossexual import BotMetrossexual
from Bots.BotTriste import BotTriste
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotDramatico import BotDramatico

###construa a lista de bots disponíveis aqui
lista_bots = [BotMetrossexual("Ken"), BotTriste("Cleber"), BotFeliz("Reef"), BotDramatico("Josemildo")]

sys = scb.SistemaChatBot("DezzBottz", lista_bots)
sys.inicio()