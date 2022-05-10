"""
Importação da biblioteca para o bot do Telegram,
Importação da classe principal
"""
import telebot
from Requests_bot import Desculpa


#Chave necessária para criação do bot fornecida belo BotFather
#ATENÇÃO: alterar para chave de seu bot
CHAVE_TOKEN = "** Coloque aqui sua chave **"
#Instancia do bot do Telegram
bot = telebot.TeleBot(CHAVE_TOKEN)

if __name__ == "__main__":
    # Instancia do objeto da classe principal
    desc = Desculpa()

    #decorator para atribuir uma nova tarefa à função
    @bot.message_handler(commands=['Family'])
    #funções responsáveis por trazer uma desculpa especifica [family, office, children, college, party]
    def family(mensagem):
        link = desc.acrescentar_na_URL(desc.url,'family/')
        desculpa = desc.devolver_desculpa(link)
        #Método responsável por responder a mensagem do usuário
        bot.send_message(mensagem.chat.id, desculpa)

    @bot.message_handler(commands=['Office'])
    def office(mensagem):
        link = desc.acrescentar_na_URL(desc.url,'office/')
        desculpa = desc.devolver_desculpa(link)
        bot.send_message(mensagem.chat.id, desculpa)

    @bot.message_handler(commands=['Children'])
    def children(mensagem):
        link = desc.acrescentar_na_URL(desc.url,'children/')
        desculpa = desc.devolver_desculpa(link)
        bot.send_message(mensagem.chat.id, desculpa)

    @bot.message_handler(commands=['College'])
    def college(mensagem):
        link = desc.acrescentar_na_URL(desc.url,'college/')
        desculpa = desc.devolver_desculpa(link)
        bot.send_message(mensagem.chat.id, desculpa)

    @bot.message_handler(commands=['Party'])
    def party(mensagem):
        link = desc.acrescentar_na_URL(desc.url,'party/')
        desculpa = desc.devolver_desculpa(link)
        bot.send_message(mensagem.chat.id, desculpa)

    # função responsável para checar as mensagens do Usuário
    def verificar(mensagem):    
        return True

    @bot.message_handler(func=verificar)
    #função responsável por apresentar as opções ao usuário
    def responder(mensagem):
        texto = '''
        Choose an excuse for:
        /Family 
        /Office 
        /Children
        /College 
        /Party
    No other option, will work, try again.
        '''
        bot.reply_to(mensagem, texto)
    # Mantém o bot em um looping infito
    bot.polling()
