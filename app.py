#encoding: utf-8
from Bots.BotImplementacao import BotImpl
from SistemaChatBot import SistemaChatBot as scb

###construa a lista de bots disponíveis aqui
lista_bots = [BotImpl("Ken", "metrossexual"), BotImpl("Cleber", "triste"), BotImpl("Reef", "feliz"), BotImpl("Josemildo", "dramatico")]

sys = scb.SistemaChatBot("DezzBottz", lista_bots)
sys.inicio()