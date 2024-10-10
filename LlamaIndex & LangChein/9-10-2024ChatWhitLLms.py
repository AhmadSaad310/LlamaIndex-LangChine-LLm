from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

#Initialize the  model
llm = Ollama(model='llama3.2')
while True:

    users = input('Ask me any Quastion: ')
    if users.lower() == 'exit':
        print('Exit')
        break

    response = llm.complete(users)
    print(response)