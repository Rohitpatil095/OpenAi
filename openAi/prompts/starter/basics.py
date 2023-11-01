import openai

openai.api_key=""

def ask_gpt(prompt, model="gpt-3.5-turbo"):
    msg =[{
            "role": "user",
            "content": prompt
         }]
    response= openai.ChatCompletion.create(
        model= model,
        message= msg,
        temperature= 0,
    )
    return response

txt= '''
    list 7 wonders 
'''
print(ask_gpt(txt))