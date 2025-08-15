# 🚀 FastAPI Setup Guide (Using venv)

Follow these steps to quickly set up and run a FastAPI project in a Python virtual environment.

---

## 1️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```
> `venv` is the name of your environment. You can choose any name.

---

## 2️⃣ Activate the Virtual Environment

```bash
source venv/bin/activate
```

---

## 3️⃣ Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

## 4️⃣ Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

---

## 5️⃣ Create Your FastAPI App

Create a file named `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

- `app = FastAPI()` creates an instance of FastAPI.
- The route `/` returns a simple JSON response.

---

## 6️⃣ Run the FastAPI App

```bash
uvicorn main:app --reload
```
- Replace `main` with your filename if different.
- `app` refers to the FastAPI instance.

---

## 7️⃣ Access Your API

- Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

> 💡 **Tip:** Use `--reload` for auto-reloading during development.

---
