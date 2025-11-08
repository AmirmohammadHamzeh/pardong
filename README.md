# 🚀 FastAPI Expense Splitter

> **A modern FastAPI-based application** for managing shared expenses, designed to simplify bill splitting, payment tracking, and data management using MongoDB and Redis.

---

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 💡 About the Project

This project was originally created to solve a common **problem in dormitories and student life** — managing shared expenses easily.  
Users can record group purchases, calculate each person’s share, and keep track of who has paid.  

It’s lightweight, scalable, and built with a **modern Python stack (FastAPI + MongoDB + Redis)**.  
The backend can also integrate with a **Telegram bot** for real-time interaction.

---

## ✨ Features

✅ RESTful API architecture (FastAPI backend)  
✅ MongoDB for storing user and expense data  
✅ Redis for caching and performance  
✅ Telegram bot integration (optional)  
✅ Dockerized setup for easy deployment  
✅ Interactive API docs via Swagger UI  

---

## 🧰 Tech Stack

**Backend:** FastAPI, Python  
**Database:** MongoDB  
**Cache:** Redis  
**Deployment:** Docker & Docker Compose  
**Optional Integration:** Telegram Bot API  

---

## ⚙️ Installation
### ⚙️ Local Setup (Dockerized)

> Run the entire project using Docker without installing Python or dependencies locally.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/pardong.git

# 2️⃣ Navigate into the project folder
cd pardong

# 3️⃣ Build and start all services with Docker Compose
docker-compose up --build

# Stop all containers
docker-compose down

# Stop containers and remove volumes (data)
docker-compose down -v
```


## 🚀 Usage

Once the app is running:
	•	Visit http://localhost:8000/docs to interact with the API.
	•	Use any HTTP client (like Postman or cURL) to test endpoints.
	•	You can also integrate the FastAPI app with your Telegram bot.



## 🖼 Screenshots

Coming soon…
(You can add screenshots or API demo images here.)



## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
To contribute:
	1.	Fork the project
	2.	Create a new branch (git checkout -b feature-name)
	3.	Commit your changes
	4.	Push to your fork and open a Pull Request



## 📜 License

This project is released under the MIT License — you are free to use, modify, and distribute it.



## 📬 Contact

Author: Amir Mohammad Hamzeh
📧 Email: amirmohammadhamzeh@outlook.com
🌐 GitHub: [AmirMohammadHamzeh](https://github.com/AmirmohammadHamzeh/)