# WhatsApp Chats Parser

A Python-based utility to parse exported WhatsApp chat messages.

## Introduction

The WhatsApp Chats Parser is a Python tool designed to parse and organize chat messages exported from WhatsApp. The tool aims to simplify the process of extracting data from exported chat logs and enables users to store this information in JSON or CSV format.

*This README.md was generated with the help of ChatGPT on `11/13/2023 - 02:40 PM`*

## Installation

1. **Clone the Repository:**
    ```
    git clone https://github.com/hirusha-adi/WhatsApp-Chats-Parser.git
    ```

2. **Open the directory:**
    ```
    cd WhatsApp-Chats-Parser
    ```

## Usage

To use the WhatsApp Chats Parser:

1. Ensure you have a chat log exported from WhatsApp.
2. Run the script `wa.py` providing the necessary arguments as described in the [Command-line Arguments](#command-line-arguments) section.

## Command-line Arguments

- `wa.py <chat_log_file>`: Parse the chat log file and display the messages in the console.
- `wa.py <chat_log_file> --json [optional_output_filename]`: Parse the chat log and save the output as JSON. If no output filename is provided, it defaults to `output.json`.
- `wa.py <chat_log_file> --csv [optional_output_filename]`: Parse the chat log and save the output as CSV. If no output filename is provided, it defaults to `output.csv`.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
