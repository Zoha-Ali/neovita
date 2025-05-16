@echo off
cd /d "C:\Study\semester4\Data Structures\project\neovita_working_prototype"
call venv\Scripts\activate.bat
set GOOGLE_API_KEY=SyDUvIl6fLV8I8fXo0QIj04C02QYv5IoE_Q
pip install google-cloud-vision
python -m streamlit run app.py
pause
