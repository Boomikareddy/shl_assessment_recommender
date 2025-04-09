# 💡 SHL Assessment Recommendation System

A web-based tool that recommends the most relevant SHL assessments based on natural language job descriptions or queries. Designed to simplify assessment selection for hiring managers.

---

## 🧑‍💻 Developer

T.Boomika

🔗 GitHub: [Boomikareddy](https://github.com/Boomikareddy)

---

## 🌐 Live Demo

- **Web App:**  
  https://shl-assessment-recommender-1-e4sh.onrender.com

- **API Endpoint:**  
  https://shl-assessment-recommender-1-e4sh.onrender.com/api/recommend?query=python+sql

---

## 📦 Project Structure

```
shl_assessment_recommender/
├── app.py                  # Flask app with form & API
├── recommender.py          # Logic to parse CSV & match queries
├── shl_data.csv            # Assessment data (name, URL, etc.)
├── requirements.txt        # Dependencies
├── .gitignore              # Ignored files (e.g., venv)
└── README.md               # This file
```

---

## 🔧 Features

✅ Takes a natural language query (e.g., "Hiring Java developer under 40 mins")  
✅ Recommends up to 10 SHL assessments  
✅ Shows test name, URL, duration, remote/adaptive support  
✅ Fully API-enabled  
✅ Deployed on Render (free-tier)  
✅ Mobile-friendly web UI with custom background and styling  

---

## 🚀 Setup Instructions (Run Locally)

1. **Clone the Repo**

```bash
git clone https://github.com/Boomikareddy/shl_assessment_recommender.git
cd shl_assessment_recommender
```

2. **Create & Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
python app.py
```

5. **Access Locally:**
- Web UI: http://127.0.0.1:5000  
- API: http://127.0.0.1:5000/api/recommend?query=python+sql

---

## ☁️ Deployment Steps (on Render)

1. Add `gunicorn` to `requirements.txt`:
   ```
   gunicorn
   ```

2. Push to GitHub:
```bash
git add .
git commit -m "Added gunicorn and cleaned project"
git push origin main
```

3. On [Render.com](https://render.com):
   - Create a new **Web Service**
   - Connect your GitHub repo
   - Set **Start command**: `gunicorn app:app`
   - Done! Your app will be deployed.

---

## 🧠 Approach Overview

### 📌 Problem Summary

Hiring managers struggle to identify SHL assessments through keyword filtering. This system accepts natural language job descriptions and intelligently recommends matching tests.

### ⚙️ Architecture Overview

**1. Data Source**  
- CSV file `shl_data.csv` containing:
  - Assessment name, URL, Remote/Adaptive Support, Duration, Type

**2. Matching Logic**  
- Python & `pandas` for querying assessments
- All query words must match `Name` column content

**3. Web App**  
- Flask routes:
  - `/` for UI form
  - `/recommend` for form POST
  - `/api/recommend` for JSON API response

**4. Deployment**  
- Render.com with auto GitHub deploy
- Gunicorn used as WSGI production server

### 🧪 Testing Examples

- `Hiring a Java developer for 40 minutes`
- `Python SQL JavaScript assessment under 1 hour`
- `Cognitive and personality tests under 45 mins`

---

## 🛠 Tech Stack

| Component     | Tool / Framework          |
|---------------|----------------------------|
| Backend       | Python, Flask              |
| Matching      | pandas                     |
| Frontend      | HTML/CSS (inline in Flask) |
| API           | Flask                      |
| Deployment    | Render + Gunicorn          |
| Source Control| Git, GitHub                |

---

## 📄 Submission Checklist

- ✅ Web App URL  
- ✅ API Endpoint  
- ✅ GitHub Repo  
- ✅ Approach Document (included in this README)

---

## 📂 License

MIT – Use it, modify it, and learn from it! 💙
