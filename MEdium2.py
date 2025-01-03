from telethon import TelegramClient, sync

# Ваші дані додатка
api_id = 21895502
api_hash = 'e0cd7ac53cfb9ee37fa75cf5c404aa60'

# Назва сесії для TelegramClient
session_name = 'MediumSession'

# Створення клієнта
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    # Підключення до Telegram
    await client.start()

    print("=== Connected to Telegram ===")
    # Отримання списку діалогів
    dialogs = await client.get_dialogs()

    print("\n=== Available chats/groups ===")
    for i, dialog in enumerate(dialogs):
        print(f"{i + 1}. {dialog.title}")

    # Вибір чату
    chat_index = int(input("\nEnter the number of the chat to interact with: ")) - 1
    selected_chat = dialogs[chat_index]

    print(f"\nSelected chat: {selected_chat.title}")

    # Отримання списку учасників
    print("\n=== Participants in the chat ===")
    participants = await client.get_participants(selected_chat)
    for participant in participants:
        print(f"- {participant.first_name} {participant.last_name or ''} ({participant.username or 'No username'})")

    # Відправлення повідомлення
    message = input("\nEnter the message to send to the chat: ")
    await client.send_message(selected_chat, message)
    print("\nMessage sent successfully!")

# Виконання програми
with client:
    client.loop.run_until_complete(main())