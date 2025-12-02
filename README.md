# 🚀 Pardong – Expense Splitter (FastAPI + Telegram Bot)

> **A modern and fully Dockerized expense-splitting system** built with **FastAPI**, **MongoDB**, **Redis**, and a **Telegram Bot**.  
> Designed to make group expense management simple, fast, and reliable.

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Bot Commands](#-bot-commands)
- [API Overview](#-api-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 💡 About the Project

**Pardong** was created to solve a very common problem among students, roommates, and families:

> *“Who owes what?”*  
> *“کی باید پول چی رو بده؟”*

This project includes:

- A **Telegram bot** for easy interaction  
- A **FastAPI backend** to handle authentication, groups, expenses, and payments  
- A **MongoDB + Redis** storage system  
- Full **Docker Compose** setup to run everything with a single command  

It is fast, scalable, and designed to be production-ready.

## ✨ Features

### ✔ Backend Features
- User registration & verification  
- Group creation and member management  
- Expense creation and participant tracking  
- Unpaid/pending expenses  
- Payment confirmation  
- Swagger API documentation  

### ✔ Bot Features
- Simple text-based UI  
- Register users and create groups  
- Add expenses  
- Split bills manually or automatically  
- View unpaid expenses  
- Confirm payments  
- Cancel ongoing interaction  

## 🤖 Bot Commands

| Command | Description |
|--------|-------------|
| **start** | ثبت‌نام کاربران |
| **user_info** | گرفتن اطلاعات کاربر |
| **register_group** | ساخت گروه |
| **add_group_members** | اضافه کردن اعضا |
| **register_expense** | ساخت خرج |
| **add_member_expense** | اضافه کردن دونگ دستی |
| **unpaid** | مشاهده لیست بدهی‌ها |
| **expenses** | مشاهده تمام خرج‌ها |
| **cancel** | لغو عملیات فعلی |

## 🔌 API Overview

Swagger UI:  
`http://localhost:8000/docs`

## 🧰 Tech Stack
Backend: FastAPI  
Database: MongoDB  
Cache: Redis  
Bot: Telegram Bot API  
Deployment: Docker & Docker Compose  
Auth: JWT Token  

## 📁 Project Structure

```
.
├── docker-compose.yml
├── pardong_bot
│   ├── Dockerfile
│   ├── main.py
│   ├── handlers/
│   ├── services/
│   ├── utils/
│   └── requirements.txt
└── pardong_fastapi
    ├── Dockerfile
    ├── main.py
    ├── routes/
    ├── Models.py
    ├── database.py
    ├── jwt_token.py
    ├── response_api.py
    └── requirements.txt
```

## ⚙️ Installation

### Docker Setup

```bash
git clone https://github.com/yourusername/pardong.git
cd pardong
docker-compose up --build
```

## 🔧 Environment Variables

Create a `.env` file:

```env
MONGO_INITDB_ROOT_USERNAME="admin"
MONGO_INITDB_ROOT_PASSWORD="password"
DB_NAME="pardong"
MONGO_URL=mongodb://${MONGO_INITDB_ROOT_USERNAME}:${MONGO_INITDB_ROOT_PASSWORD}@mongodb:27017/?authSource=admin

REDIS_HOST="redis"
REDIS_PORT=6379

PORT=8000
SECRET_KEY="d1d88dfc56771f84c62e557a397ff3b4dde5fda1d5fbd42fb3d7a5955a451fb9"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

TELEGRAM_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
```

## 🚀 Usage

FastAPI Docs:  
`http://localhost:8000/docs`

Telegram bot:  
Start the bot and use the commands.

## 🖼 Screenshots
Coming soon…

## 🤝 Contributing
Fork → Branch → Commit → PR

## 📜 License
MIT License

## 📬 Contact
Author: **Amir Mohammad Hamzeh**  
Email: **amirmohammadhamzeh@outlook.com**  
GitHub: https://github.com/AmirmohammadHamzeh
