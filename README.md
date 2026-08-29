# React + FastAPI Full-Stack Application

A modern full-stack web application built with a **FastAPI** Python backend and a **React** (Vite) frontend.

---

## 🚀 Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python) + Uvicorn
- **Frontend:** [React](https://react.dev/) + [Vite](https://vitejs.dev/) + Axios
- **Communication:** REST API with CORS configured

---

## 📁 Project Structure

```text
React-FastAPI/
│
├── backend/            # FastAPI Backend
│   ├── venv/           # Python Virtual Environment
│   ├── main.py         # FastAPI application entry point
│   └── ...
│
└── frontend/           # React Frontend (Vite)
    ├── src/
    └── ...
```

---

## 🛠️ Getting Started & Installation

Follow these steps to set up and run the project locally on your machine.

### Prerequisites
- Python (v3.8 or higher)
- Node.js & npm (or yarn)

---

### 1. Clone the Repository
```bash
git clone https://github.com/awaistechy/React-FastAPI.git
cd React-FastAPI
```

---

### 2. Backend Setup (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Mac / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

4. Run the FastAPI server:
   ```bash
   python main.py
   # OR using uvicorn directly:
   # uvicorn main:app --reload
   ```

- The backend will run at **`http://localhost:8000`**.
- Interactive API documentation (Swagger UI) is available at **`http://localhost:8000/docs`**.

---

### 3. Frontend Setup (React)

1. Open a new terminal window and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

- The frontend will run at **`http://localhost:5173`**.

---

## ⚙️ Configuration Note (CORS)

To allow the React frontend (`http://localhost:5173`) to communicate smoothly with the FastAPI backend (`http://localhost:8000`), make sure `CORSMiddleware` is configured in your backend `main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
