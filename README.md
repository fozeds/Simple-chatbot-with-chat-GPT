Simple Chat GPT
---------------

Este script é um chatbot baseado no GPT-3. Ele permite que você faça perguntas e obtenha respostas geradas pelo modelo.

### Requisitos

*   Uma chave de API válida da OpenAI (você pode criar uma em [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys))
*   Python 3.6 ou superior
*   Biblioteca PySimpleGUI (pode ser instalada com o comando `pip install pysimplegui`)
*   Biblioteca openai (pode ser instalada com o comando `pip install openai`)

### Como usar

1.  Execute o script no terminal ou prompt de comando
2.  Insira sua chave de API quando solicitado
3.  Faça perguntas para o chatbot na caixa de entrada e pressione o botão "Enviar" ou aperte Enter
4.  Veja as respostas geradas pelo GPT-3 na caixa de saída
5.  Pressione o botão "Sair" para fechar o programa

### Personalizando

Você pode escolher qual modelo do GPT-3 deseja usar na sua sessão de chat. Para fazer isso, altere a linha `self.model = "text-davinci-003"` para o modelo desejado. Os modelos disponíveis são:

*   text-davinci-003
*   text-curie-001
*   text-babbage-001
*   text-ada-001

### Importante

Observe que, como este script é baseado no GPT-3, as respostas geradas podem conter conteúdo inapropriado ou impróprio. Use-o com cuidado e moderação.
