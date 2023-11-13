import re
import argparse
import json
import csv


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


def save_to_json(messages, output_file):
    with open(output_file, 'w') as file:
        json.dump(messages, file, indent=4)


def save_to_csv(messages, output_file):
    keys = messages[0].keys() if messages else []
    with open(output_file, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(messages)


def main():
    parser = argparse.ArgumentParser(description='WhatsApp Chat Parser')
    parser.add_argument('input_file', help='Input file name')
    parser.add_argument('--json', dest='json', nargs='?',
                        const='output.json', default=None, help='Output as JSON')
    parser.add_argument('--csv', dest='csv', nargs='?',
                        const='output.csv', default=None, help='Output as CSV')

    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        chat_text = file.read()

    parsed_messages = parse_whatsapp_chat(chat_text)

    if args.json:
        if args.json == 'output.json':  # Default filename
            output_file_json = args.json
        else:
            output_file_json = args.json + \
                ('.json' if not args.json.endswith('.json') else '')
        save_to_json(parsed_messages, output_file_json)
        print(f'Parsed data saved to {output_file_json} as JSON.')

    if args.csv:
        if args.csv == 'output.csv':  # Default filename
            output_file_csv = args.csv
        else:
            output_file_csv = args.csv + \
                ('.csv' if not args.csv.endswith('.csv') else '')
        save_to_csv(parsed_messages, output_file_csv)
        print(f'Parsed data saved to {output_file_csv} as CSV.')


if __name__ == '__main__':
    main()
