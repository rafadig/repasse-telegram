from telethon import TelegramClient, sync, events

# Aqui você vai colocar a API e Hash do Telegram, se você não sabe como pegar é só dar um GOOGLE
api_id = 'SEU_API_ID'
api_hash = 'SEU_API_HASH'
sessao = 'Repassar Mensagem'

def main():
    print('Monitoramento iniciado ...')
    client = TelegramClient(sessao, api_id, api_hash)

# Aqui você vai trocar esse sequencia de 0 pelo ID do grupo que você quer copiar
    @client.on(events.NewMessage(chats=[0000000000]))
    async def enviar_mensagem(event):
        texto_mensagem = event.raw_text

        # Substituir palavras ou frases (filtro de palavras)
        texto_mensagem = texto_mensagem.replace('FRASE OU PALAVRA QUE VOCÊ NÃO QUER', 'SUA FRASE')
        texto_mensagem = texto_mensagem.replace('FRASE OU PALAVRA QUE VOCÊ NÃO QUER', 'SUA FRASE')
        texto_mensagem = texto_mensagem.replace('FRASE OU PALAVRA QUE VOCÊ NÃO QUER', 'SUA FRASE')

        
        #E por ultimo você troca as duas sequencias de 0 pelo ID do grupo que vai receber as mensagens
        if event.media:
            await client.send_file(0000000000, file=event.media, caption=texto_mensagem)
        else:
            await client.send_message(0000000000, texto_mensagem)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
