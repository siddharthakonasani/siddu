# Reddit User Persona Generator 

This project is a submission for an AI/LLM Engineer Internship assignment by BeyondChats. It demonstrates LLM-assisted behavioral analysis and persona generation using real Reddit user data. The goal is to model user behavior for NLP/UX purposes through content filtering, trait extraction, and persona writing.

---

# Objective

Create a script that:
1. Takes a Reddit username as input
2. Extracts all posts and comments using Reddit's API
3. Cleans and filters the data
4. Outputs a detailed, citation-backed user persona in plain text

---

# Tech Stack

- Python 3.10+
- `praw` (Python Reddit API Wrapper)
- `python-dotenv` (for secure credentials)
- Manual & LLM-assisted content analysis
- Citation-based persona documentation

---

# Project Structure

reddit-persona-project/
├── **main.py** # Main script for data scraping and cleaning
├── print_cleaned.py # Utility to print or save cleaned data
├── **.env** # Reddit API credentials (not included)
├── **kojied_cleaned.json** # Cleaned JSON for Reddit user kojied
├── **hungry-move-6603_cleaned.json** # Cleaned JSON for Reddit user Hungry-Move-6603
├── **kojied_persona_final_report.txt** # Final persona for user kojied
├── **hungry-move-6603_persona_final_report.txt** # Final persona for user Hungry-Move-6603
└── **README.md** # You're reading this


---

# How to Run

1. Set up your `.env` file with Reddit credentials:
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_user_agent


2. Install dependencies:
bash
pip install praw python-dotenv


3. Run the script with a Reddit profile URL:
bash
python main.py https://www.reddit.com/user/kojied/

4. Preview cleaned data (optional):
bash
python print_cleaned.py

# Deliverables
File	Description
kojied_persona_final_report.txt------------Deep philosophical, tech-aware persona
hungry-move-6603_persona_final_report.txt--Regional, blunt, civic-minded persona

# Highlights
>Fully functional Reddit data pipeline
>Human + LLM co-generated personas
>Product-ready language and insights
>Citations included for every trait
>ATS-safe, prompt-tuning optimized output

# Key Skills Demonstrated
>User modeling and segmentation
>Prompt engineering awareness
>AI UX research and behavioral profiling
>Real-world data cleaning and filtering
>NLP-aligned persona writing

# Notes
This project was built as part of an AI internship assessment. All personas were created using publicly available Reddit content and structured for ethical AI and product design use cases.

Author: **Siddhartha Ram Konasani**
Mail: siddharthakonasani.77@gmail.com
Date: 14-July 2025
Submitted for: AI/LLM Engineer Internship Assessment by BeyondChats
