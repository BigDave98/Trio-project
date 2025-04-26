# 📬 Mailchimp Contact Sync

This project is a backend service that synchronizes user contact data from a public MockAPI to a Mailchimp list.
It fetches first name, last name, and email from the MockAPI and creates subscribers on Mailchimp.

---

## 📄 Technical Design

📄 Technical Design Document
You can find the Technical Design here: https://docs.google.com/document/d/1E5SKYuRdy0bSrpib-H1rzo99GIJTqw4GmQ74HAhNoSM/edit?tab=t.0#heading=h.ngj6uth22xd8

The document includes:

Project flow

Folder architecture

Tech stack justifications

Alternatives considered

---

## 🚀 Demo

✅ Deployed on Railway: https://trio-project-production.up.railway.app

---

## 🎥 Video Walkthrough

VIDEO LINK

In this video I explain:
- How the software works
- Why I chose this structure and libraries
- A walkthrough of syncing data from MockAPI to Mailchimp

---

## 🧠 Features

- Fetches contacts from MockAPI
- Adds new members to a Mailchimp list
- Reads from environment variables
- Clean and minimal Flask structure
- Fully containerized with Docker
- Basic HTML UI for manual triggering

---

## 📂 Endpoints

### `GET /contacts/sync`
Returns a list of synced contacts currently in Mailchimp.
```json
{
  "syncedContacts": 25,
  "contacts": [
    { "first_name": "Davi", "last_name": "Ruas", "email": "davi@example.com" },
    ...
  ]
}
```

### `POST /contacts/add`
Fetches contacts from MockAPI and adds them to Mailchimp.

---

## 🏗️ Architecture
```bash
/app
  ├── __init__.py
  ├── routes.py
  ├── utils.py
  ├── mockapi/
  │    └── mockapi.py
  └── mailchimp/
       └── mailchimp_SDK/
           ├── add_members.py
           ├── retrieve_members.py
           └── utils.py
/tests
  ├── test_mockapi.py
  ├── test_mailchimp.py
  └── test_routes.py
/static
  └── styles.css
/templates
  └── index.html
Dockerfile
docker-compose.yml
.dockerignore
.env.example
requirements.txt
README.md
```

## 🛠 How to Run Locally

```bash
# 1. Clone the project
$ git clone https://github.com/seu-usuario/seu-repo.git
$ cd your-repo

# 2. Create your environment
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the Flask server
$ flask run
```

Then visit: `http://localhost:5000`

---

## 🧪 Tests

```bash
# Run all tests
$ pytest --cov=app --cov-report=term-missing
```

---

## 🐳 Docker

To run the project using Docker, you'll need:
- Docker installed ([Install Docker](https://docs.docker.com/get-docker/))
- Loggin Docker

```bash
# Build the Docker image
docker build -t mailchimp-sync .

# Run the container with environment variables
docker run -p 8000:8000 --env-file .env mailchimp-sync
```

Then visit: `http://localhost:8080`

---

## ⚙️ Environment Variables

```env
MAILCHIMP_API_KEY=b6c4c5bf7636f562cb60b3d28a88b5ea-us8
MAILCHIMP_PREFIX=us8
MAILCHIMP_LIST_ID=8c21538296
MOCKAPI_URL=https://challenge.trio.dev/api/v1/contacts
```

---

## 📬 Contact

Made by **Davi Ruas** – [daviruastb@gmail.com](mailto:daviruastb@gmail.com)

> Designed with simplicity and clarity to match real-world API integration scenarios.
