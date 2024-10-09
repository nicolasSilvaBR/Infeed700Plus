@echo off
:: Start main.py on port 8501 in the background
start /b "" streamlit run main.py --server.port 8501

:: Start documentation.py on port 8504 in the background
start /b "" streamlit run documentation.py --server.port 8504

:: Start testPage.py on port 8503 in the background
start /b "" streamlit run testPage.py --server.port 8503

exit
