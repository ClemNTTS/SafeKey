# SAFEKEY - Secure API Key Management

**SAFEKEY** is a tool designed for the secure management and storage of API keys and other critical secrets. It provides encrypted storage, easy key management, and seamless environment variable injection, helping you keep your credentials safe and accessible.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Encrypted Storage**: Securely store API keys and passwords.
- **Key Management**: Add, delete, and retrieve keys effortlessly.
- **Environment Variable Injection**: Inject keys as environment variables for easy use in your applications.
- **User Interface**: Simple interface for managing your keys.

## Prerequisites

- Python 3.7 or later
- [Pip](https://pip.pypa.io/en/stable/) (Python package manager)
- [SQLite](https://www.sqlite.org/index.html) (or other configured database)

## Installation

To install **SAFEKEY**, follow these steps:

1. **Clone the repository**:

We higly recommand to set it in the base directory of all your projects to acces them, like in your directory ../User/user_name/

```bash
git clone https://github.com/ClemNTTS/SAFEKEY.git
```

2. **Navigate to the project directory**:

   ```bash
   cd SAFEKEY
   ```

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the dependencies**:

   ```bash
   pip install cryptography
   pip install pyperclip
   ```

5. **Run SAFEKEY**:

   ```bash
   python safekey.py
   ```

## Usage

1. **Check all database**:

   ```bash
   cd data/
   ls
   ```

2. **See Keys**:

- You have to set the right password, use option 2 to reset it.
- Option 3 allow you to watch all your keys decrypted.
- It's a good way to check if you have set the right password

3. **Inject Keys as Environment Variables**:

- In MENU, press 8 and Enter
- The program should ask for the data base name and key name.
- The program ask the path of your project.

- The program install your env variable or print an error if there is a problem

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [clement.nutt@gmail.com](mailto:clement.nutt@gmail.com).

Project Link: [https://github.com/ClemNTTS/SAFEKEY](https://github.com/ClemNTTS/SAFEKEY)
