from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIGURACOES_CONVERSAS = [
    "/home/mateus/Documentos/python/robo_chat/conversas/saudacoes.json",
    "/home/mateus/Documentos/python/robo_chat/conversas/informacoes_basicas.json"  
]

def iniciar():
    robo = ChatBot("Robô de Atendimento Edm Comércio de frutas")
    treinador = ListTrainer(robo)
    
    return robo, treinador
    
def carregar_conversas():
    conversas = []
    
    for arquivo_configuracao in CONFIGURACOES_CONVERSAS:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas.append(json.load(arquivo)['conversas'])
            
            arquivo.close()
    return conversas

def treinar_robo(treinador, conversas):
    for conversa in conversas:
        #print(conversa)
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta['mensagens']
            #print(mensagens)
            resposta = mensagens_resposta['resposta']

            #print(f"treinando o robô a: '{mensagens}' com a resposta: '{resposta}'")
            for mensagem in mensagens:
                
                print(mensagem)
                print(resposta)
                #treinador.train([mensagem, resposta])

def main():
    _, treinador = iniciar()
    
    conversas = carregar_conversas()
    
    if conversas:
        treinar_robo(treinador, conversas)

if __name__ == "__main__":
    main()