import openai

resposta = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
    messages = [
      {
       "role" : "system",
         "content" : "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
      },
      {
       "role" : "user",
         "content" : "Gere 5 produtos"
         }
    ]
)

print(resposta)
