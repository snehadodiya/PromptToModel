# 🤖 Prompt2ML – Turn Natural Language into ML Code with LLMs

A smart full-stack web app that turns your **dataset and ML prompt** into a complete, executable machine learning project. From Python scripts to output files and documentation, it auto-generates everything you need — ready to run and download instantly.

---

## 🔍 Highlights

- 🧠 Tested with **50+ prompts** across tasks like classification, regression, EDA, and time series  
- 📂 Handles **10+ structured datasets** (.csv/.xlsx) with smart header extraction  
- ✅ Achieved **90%+ success rate** from input prompt to fully working ML pipeline  
- ⚡ Fast responses — generates code in around **5 seconds**  
- 📦 Outputs **7+ development-ready files** per session (`.py`, `.txt`, `.png`, `.md`)  
- 🔧 Requires **no manual tweaking** for over **85%** of use cases

---

## 🎬 Demo Walkthrough

▶️ Check out how it works:  
**[🔗 YouTube Video](https://youtu.be/fQ3WwxZrl2o?si=xS1kZCKHAPhA07o-)**

---

### 💡 Tech Behind the Project

- ⚛️ **Frontend**: React + Material UI  
- 🐍 **Backend**: Python (ML engine), Node.js, Express  
- 🧠 **LLM Integration**: OpenRouter API + Mixtral LLM

---

## 🧠 What This App Does

1. **Upload** a `.csv` or `.xlsx` dataset  
2. **Type a natural prompt** like:  
   _“Build a regression model for predicting house prices”_
3. The app:
   - Parses and analyzes the file
   - Sends input to an LLM via OpenRouter
   - Receives clean, structured Python code
   - Executes it to produce plots, summaries, and results
4. **Get a downloadable ZIP** with:
   - Dataset copy
   - ML scripts (`step_1_train_model.py`, etc.)
   - Output files (plots, text)
   - A unified `pipeline.py`
   - README and requirements

---

## 🚀 Sample Prompts

| Prompt                        | Output Generated                        |
|------------------------------|-----------------------------------------|
| Build a churn prediction model | Trained classifier, accuracy score     |
| Run exploratory data analysis  | Summary stats, heatmaps, distribution plots |
| Visualize monthly sales trends | Time series plots using matplotlib     |
| Train a price predictor        | Regression model with MSE/R2 results   |

---

## 🛠️ Tech Stack

### Frontend  
- React  
- Material UI  

### Backend  
- Node.js + Express  
- Python ML Engine  
- `child_process` to run Python  
- `multer` for uploads  
- `archiver` to generate ZIP  

### LLM Integration  
- OpenRouter API  
- Mixtral-8x7B-Instruct  

---

## 📦 What You Get in the ZIP


> Download once, and run everything via `pipeline.py` – it's all pre-generated and linked.
dataset.csv
step_1_train_model.py, step_2_plot_accuracy.py...
output_step_X.png or .txt
pipeline.py (chained runnable version)
README.md and requirements.txt
---

## 🔐 API Access

You’ll need a free API key from OpenRouter to get started:

🔗 Get yours at: https://openrouter.ai/

---

## 🌟 What’s Coming Next

- Toggle between multiple LLMs (GPT-4, Claude, Mixtral, etc.)
- Visual dashboard to display plots and stats
- Secure Python sandbox for code execution
- Real-time collaboration with chat + history
- Deployment options via HuggingFace/Render

---

## 🙌 Credits

Created with 💡 by **Sneha Dodiya** — a passionate full-stack developer exploring AI, automation, and real-world ML solutions through intuitive user experiences.

---

