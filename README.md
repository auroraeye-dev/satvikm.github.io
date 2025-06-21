# 👨‍💻 Satvik Mishra | GitHub Portfolio

Welcome to my technical project portfolio! I’m an engineer exploring and building tools in **cloud computing, cybersecurity, data architecture, and AI**. This repository includes working projects, documentation, and automation scripts I’ve created or compiled.

---

## 🧠 AI Voice Assistant – Beast 🧠

A personal assistant powered by speech recognition, GPT-3.5, News API, and automation libraries like `pyautogui`.

🔹 Features:
- Voice-controlled Google/Youtube/Instagram/etc.
- Music playback with skip-ad support
- News fetching via NewsAPI
- OpenAI GPT-3.5 responses to custom prompts

📁 Files:
- `beast_ai.py`  
- `musiclibrary.py`  
- `openaiintegration.py`  
- `skip_button.py`  
- `google_search.py`  

📸 Example command:  
> “Wake up” → “Open YouTube” → auto skips ads → responds to follow-ups using AI.

📎 Dependencies: `speech_recognition`, `pyttsx3`, `pyautogui`, `openai`, `newsapi`

---

## ☁️ AWS Deployment & Monitoring Automation

📄 `AWS Deployment and Monitoring Automation using VS Code.docx`

A detailed technical document outlining:
- Steps to deploy applications on AWS using Visual Studio Code
- Monitoring with AWS CloudWatch and dashboards
- DevOps CI/CD integration options

---

## 🌐 AWS Site-to-Site VPN Setup

📄 `AWS site to site VPN.website.docx`

A beginner-to-advanced guide for configuring:
- Site-to-site VPN on AWS
- Tunnel configuration, route tables, and testing
- Security best practices

---

## 🧱 Data Lake vs Lakehouse (Medallion Architecture)

📄 `upload_data_doc.docx`

A concept and architecture breakdown:
- Difference between data lake, warehouse, and lakehouse
- Medallion architecture (Bronze, Silver, Gold layers)
- Implemented using **Databricks + Delta Lake**

Useful for those exploring modern data engineering pipelines.

---

## 🔎 OpenAI + Google Search Automation

🧠 `openaiintegration.py`  
🌍 `google_search.py`  

Combines LLM-generated queries with automated Google search. You speak → GPT refines → searches Google → displays top results.

---

## ⏩ YouTube Ad Skipper (Image-based)

📌 `skip_button.py`  
🖼 Requires screenshot image of “Skip Ad” button

Uses `pyautogui` to find the button and click it automatically after timeout.

---

## 🔧 Tools Used Across Projects

- Python 3.10+
- Libraries: `speech_recognition`, `pyttsx3`, `openai`, `pyautogui`, `newsapi-python`, `requests`
- Platform: Windows 10+ (with mic access)
- IDEs: VS Code, Jupyter Notebook
- Cloud: AWS (EC2, S3, CloudWatch, Site-to-Site VPN)

---

## 📁 Folder Summary

```txt
.
├── beast_ai.py
├── musiclibrary.py
├── google_search.py
├── openaiintegration.py
├── skip_button.py
├── AWS Deployment and Monitoring Automation using VS Code.docx
├── AWS site to site VPN.website.docx
├── upload_data_doc.docx
└── README.md  <-- You are here
