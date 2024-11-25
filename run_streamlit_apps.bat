@echo off
:: Start main.py on port 8501 in the background
start /b "" streamlit run main.py --server.port 8505

:: Start documentation.py on port 8504 in the background
start /b "" streamlit run functions/documentation.py --server.port 8506

exit
