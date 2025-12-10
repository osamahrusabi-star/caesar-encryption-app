# Caesar Cipher Web Application

A modern web application that implements the classic Caesar Cipher encryption technique with a beautiful user interface built with Django.

## Features

- 🔐 Encrypt and decrypt text using Caesar Cipher
- 🎨 Modern, gradient-based UI design
- 📱 Responsive design for mobile and desktop
- ⚡ Fast, client-server architecture using Django
- 📋 Copy result functionality

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Django development server:
```bash
python manage.py runserver
```

2. Open your browser and navigate to:
```
http://127.0.0.1:8000
```

3. Enter your message, choose a shift value (0-25), and click Encrypt or Decrypt!

## How Caesar Cipher Works

The Caesar Cipher is one of the simplest encryption techniques. It shifts each letter in the text by a fixed number of positions in the alphabet. For example, with a shift of 3:
- A → D
- B → E
- C → F
- ...and so on

## Project Structure

```
caesar-cipher/
├── manage.py              # Django management script
├── caesar_cipher.py       # Encryption/decryption logic
├── requirements.txt       # Python dependencies
├── caesar_project/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cipher/                # Django app
│   ├── views.py          # View functions
│   └── urls.py           # App URLs
├── templates/
│   └── index.html        # HTML frontend
└── static/
    └── style.css         # CSS styling
```

## Technologies Used

- **Backend**: Python, Django 5.1
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: Gradient backgrounds, modern UI/UX

## License

Free to use and modify!
