# 🏋️ Fitness API

![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/fitness-api)
![GitHub license](https://img.shields.io/github/license/yourusername/fitness-api)

**Fitness API** is a RESTful API built with Django, Django REST Framework (DRF), and PostgreSQL to manage workouts, users, and fitness tracking. The API supports **OAuth2 authentication**, **automated AI-generated workout plans**, and **real-time tracking**.

---

## 🚀 Features

- 🏋️ **Workout Plans** - Create, update, and track custom workout plans.
- ✅ **AI-Generated Workouts** - Uses OpenAI's GPT-4 to generate custom workout routines.
- 🔑 **OAuth2 Authentication** - Secure login using `django-allauth` and `django-oauth-toolkit`.
- 📊 **Progress Tracking** - Track nutrition, exercises, and daily progress.
- 🌍 **API Documentation** - Swagger and Redoc integration.
- 🛠 **Production Ready** - Built for DigitalOcean deployment with Gunicorn & Nginx.

---

## 📂 Project Structure

```bash
├── core
│   ├── models
│   ├── views
│   ├── serializers
│   ├── services
│   ├── signals
│   ├── tests
│   ├── docs.py  # API Documentation
│   ├── urls.py
│   ├── wsgi.py
├── static  # Static files for deployment
├── templates  # Admin & API docs
├── manage.py
└── README.md
```

---

## 🛠 Installation & Setup

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/yourusername/fitness-api.git && cd fitness-api
```

### **2️⃣ Set up a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # macOS & Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Set up environment variables**

Create a `.env` file with the following:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/fitness_db
OPENAI_API_KEY=your-openai-api-key
```

### **5️⃣ Run database migrations**

```bash
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### **6️⃣ Run the development server**

```bash
python manage.py runserver
```

Now, your API is running at `http://127.0.0.1:8000/api/v1/`

---

## 📜 API Documentation

This API uses **Swagger and ReDoc** to document all available endpoints.

- **Swagger UI**: [http://127.0.0.1:8000/api/docs/swagger](http://127.0.0.1:8000/api/docs/swagger)
- **ReDoc**: [http://127.0.0.1:8000/api/docs/redoc](http://127.0.0.1:8000/api/docs/redoc)

To update the API documentation, run:

```bash
python manage.py spectacular --format openapi-json > api-docs.json
```

---

## 🚀 Deployment

This project is **production-ready** and built for **DigitalOcean, Gunicorn, and Nginx**.

### **1️⃣ Docker Setup (Optional)**

```bash
docker build -t fitness-api .
docker run -p 8000:8000 fitness-api
```

### **2️⃣ Deploy to DigitalOcean**

```bash
ssh root@your-server-ip
cd /opt/fitness-api
git pull origin main
sudo systemctl restart gunicorn
```

### **3️⃣ Set up GitHub Actions for Auto Deployment**

A `.github/workflows/deploy.yml` file will be configured for **CI/CD automation**.

---

## ✅ Running Tests

Before deployment, ensure all tests pass:

```bash
pytest
```

Run specific tests:

```bash
pytest core/tests/test_workout_plans.py
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Support & Contact

📧 Email: <support@yourdomain.com>  
🌐 Website: [yourdomain.com](https://yourdomain.com)
