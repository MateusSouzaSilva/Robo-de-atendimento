from chatterbot import ChatBot


def executar_robo():
    robo = ChatBot("Robô de Atendimento Edm Comércio de frutas")
    
    while True: 
        entrada = input("digite alguma coisa...\n")
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.6:
            print(resposta.text)
        else:
            print("Ainda não sei como responder essa pergunta")
            print("Pergunte outra coisa")
    
if __name__ == "__main__":
    executar_robo()
