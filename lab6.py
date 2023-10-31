import unittest
import telebot
from lab5 import bot 
from lab5 import send_silver_sword_info  

class TestBotFunctionality(unittest.TestCase):

    # Тест для функции send_silver_sword_info.
    def test_send_silver_sword_info(self):
        # Создаем объект сообщения для имитации сообщения от пользователя
        class Message:
            def __init__(self, chat_id):
                self.chat_id = chat_id
                self.text = "Серебреные Мечи"

        # Имитируем сообщение от пользователя
        message = Message(713901266)  
        result = send_silver_sword_info(message.chat_id, 0, bot)

        # Проверяем, что результатом является строка (не None)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
