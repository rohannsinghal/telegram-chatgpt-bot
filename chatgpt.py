import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai

class Reference:
    def __init__(self) -> None:
        self.response = ""

load_dotenv()

openai.api_key = 'xxxxxxxxxxxxxxx'

reference = Reference()

TOKEN = os.getenv("7213609841:AAEdExt20ozX0kfelnsmx9w6uXEHapOBoe8")

MODEL_NAME = "gpt-3.5-turbo"

bot = Bot(token='7213609841:AAEdExt20ozX0kfelnsmx9w6uXEHapOBoe8')
dispatcher = Dispatcher(bot)

def clear_past():
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    clear_past()
    await message.reply("Hello! \nI'm chatGPT Telegram bot created by Rohan!\
                        \nHow may I assist you today?")

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """ 
    Hi there, I'm chatGPT bot created by Sunny! Please follow these commands -
    /start - to start the conversation 
    /clear - to clear the past conversation and context. 
    /help  - to get this help menu. 
    I hope this helps.
    """
    await message.reply(help_command)

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    print(f">» USER: \n{message.text}")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">» chatGPT: \n{reference. response}")
    await bot.send_message(chat_id=message.chat.id, text=f"{reference.response}")


if __name__ == '__main__':
    print("Starting...")
    executor.start_polling(dispatcher, skip_updates=True)
    print("Stopped")