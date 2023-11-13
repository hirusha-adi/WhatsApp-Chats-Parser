import re


def parse_whatsapp_chat(chat_text):
    messages = []

    group_creation_pattern = re.compile(
        r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*?) created group “(.*?)”')
    member_addition_pattern = re.compile(
        r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*?) added (.*?)')

    pattern = re.compile(r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*?): (.*)')
    attachment_pattern = re.compile(
        r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (.*?): (.*) \((file attached)\)')

    lines = chat_text.split('\n')

    for line in lines:
        group_creation_match = group_creation_pattern.match(line)
        if group_creation_match:
            timestamp = group_creation_match.group(1)
            creator = group_creation_match.group(2)
            group_name = group_creation_match.group(3)
            messages.append({
                'timestamp': timestamp,
                'creator': creator,
                'action': f"created group '{group_name}'"
            })
        else:
            member_addition_match = member_addition_pattern.match(line)
            if member_addition_match:
                timestamp = member_addition_match.group(1)
                user = member_addition_match.group(2)
                added_member = member_addition_match.group(3)
                messages.append({
                    'timestamp': timestamp,
                    'user': user,
                    'action': f"added {added_member}"
                })
            else:
                attachment_match = attachment_pattern.match(line)
                if attachment_match:
                    timestamp = attachment_match.group(1)
                    sender = attachment_match.group(2)
                    message = attachment_match.group(3)
                    messages.append({
                        'timestamp': timestamp,
                        'sender': sender,
                        'message': message,
                        'is_file': True
                    })
                else:
                    match = pattern.match(line)
                    if match:
                        timestamp = match.group(1)
                        sender = match.group(2)
                        message = match.group(3)
                        messages.append({
                            'timestamp': timestamp,
                            'sender': sender,
                            'message': message,
                            'is_file': False
                        })

    return messages


if __name__ == "__main__":
    chat_text = """
Messages to this group are now secured with end-to-end encryption.
13/11/2023, 08:10 - Loris created group “WhatsApp Chat Parser Example”
13/11/2023, 08:10 - Loris added Emily
13/11/2023, 08:10 - Loris added John
13/11/2023, 08:11 - adikari: This is a test msg - like kela wuna
13/11/2023, 08:11 - adikari: testing
13/11/2023, 08:12 - adikari: 🥹🥹
13/11/2023, 08:12 - adikari: 🥹emoji with text 🥹
13/11/2023, 08:12 - hirusha: lol
13/11/2023, 08:12 - adikari: STK-20230920-WA0004.webp (file attached)
13/11/2023, 08:12 - hirusha: STK-20230726-WA0005.webp (file attached)
13/11/2023, 08:36 - adikari: sample text
13/11/2023, 08:36 - hirusha: not a sample text?
13/11/2023, 08:36 - hirusha: testing LOL
13/11/2023, 08:36 - hirusha: IMG-20231113-WA0025.jpg (file attached)
I use something like this to see who touched my phone and tried to unlock it
13/11/2023, 09:00 - adikari: Adeee
13/11/2023, 13:21 - hirusha: Hi Moko wune?
"""

    parsed_messages = parse_whatsapp_chat(chat_text)

    for msg in parsed_messages:
        if 'creator' in msg:
            print(f"At {msg['timestamp']}, {msg['creator']} {msg['action']}")
        elif 'user' in msg:
            print(f"At {msg['timestamp']}, {msg['user']} {msg['action']}")
        else:
            print(f"At {msg['timestamp']} - {msg['sender']}: {msg['message']}")
            if 'is_file' in msg and msg['is_file']:
                print("File Attached")
        print("------")
