# Infeed700 Application Documentation
# Python Version 3.12.5

## Table of Contents

1. [Overview](#overview)
2. [Installation Instructions](#installation-instructions)
3. [Required Software and Libraries](#required-software-and-libraries)
    - [Python](#1-python)
    - [pip (Python Package Installer)](#2-pip-python-package-installer)
    - [Pre-downloaded Python Dependencies (.whl files)](#3-pre-downloaded-python-dependencies-whl-files)
    - [Streamlit](#4-streamlit)
4. [Python Naming Conventions and Best Practices](#python-naming-conventions-and-best-practices)
    - [1. Naming Python Files](#1-naming-python-files)
    - [2. Naming Functions](#2-naming-functions)
    - [3. Naming Variables](#3-naming-variables)
    - [4. Naming Classes](#4-naming-classes)
    - [5. Naming Constants](#5-naming-constants)
    - [6. Private Methods and Variables](#6-private-methods-and-variables)
    - [7. Naming Test Files and Functions](#7-naming-test-files-and-functions)
    - [8. General Guidelines](#8-general-guidelines)
5. [Setting Up Automatic Background Execution of Streamlit Apps on Windows](#setting-up-automatic-background-execution-of-streamlit-apps-on-windows)

---

## Overview

The **Infeed700** application is an interactive platform developed by **ICMC Solutions** using **Streamlit**. It provides embedded dashboards and **SSRS** (SQL Server Reporting Services) reports, allowing users to access and visualize data efficiently in an on-premises environment. This application is designed to serve multiple clients, offering a user-friendly and responsive interface.

---

## Installation Instructions

Follow these steps to set up the **Infeed700** application on your local machine:

1. **Download Python**:
   - Visit the official Python website: [**Download Python**](https://www.python.org/downloads/).
   - Download the latest version of **Python** (make sure to choose the installer compatible with your operating system).
   - Run the installer and make sure to check the box that says **"Add Python to PATH"** during installation.

2. **Download and Extract the Application Files**:
   - Download the **Infeed700** application files, which are provided as a `.zip` or `.rar` archive.
   - Extract the contents of the archive to a local directory of your choice.

3. **Navigate to the Application Directory**:
   - Open a **command prompt** window (you can do this by searching for **"cmd"** in the Windows search bar).
   - Use the `cd` command to change to the directory where you extracted the application files. For example:
     ```bash
     cd path\to\your\extracted\folder
     ```

4. **Run the Setup Batch File**:
   - In the **command prompt**, execute the `setup.bat` file by typing:
     ```bash
     setup.bat
     ```
   - This will install all the required dependencies and start the **Streamlit** application.

5. **Access the Application**:
   - After running the setup, the **Streamlit** application should automatically launch in your web browser. If it doesn't, you can manually open your browser and go to `http://localhost:8501`.

By following these steps, you will have the **Infeed700** application set up and running on your local machine. If you encounter any issues, please refer to the troubleshooting section of this documentation or seek assistance from your IT support team.

---

## Required Software and Libraries

To run the batch file you provided, the following software and libraries are required:

### 1. Python:
- **Version**: Python should be installed on the machine. The batch file checks if Python is installed using `python --version`. You can download Python from [https://www.python.org/](https://www.python.org/).
- **Ensure Python is in your system's PATH**: So it can be accessed from the command line. If it's not, the batch file will fail with the error message "Python is not installed or not found in the PATH."

### 2. pip (Python Package Installer):
- **Installed with Python**: Pip comes installed by default with Python. It is used to install the `.whl` files (Python wheel files) found in the `libs` folder. The command `pip install --no-index --find-links="%LIBS_DIR%" "%%f"` is used to install these dependencies without fetching from the internet.

### 3. Pre-downloaded Python Dependencies (.whl files):
- You need to have pre-downloaded Python wheel (`.whl`) files for all required packages stored in the `libs` directory. These `.whl` files must be compatible with your Python version and system architecture. The batch file installs each `.whl` file found in the `libs` folder using `pip`.

### 4. Streamlit:
- **Python package**: The batch file assumes that your project uses Streamlit, a Python-based web application framework. One of the `.whl` files in the `libs` folder should be `streamlit`. You will also need any other dependencies required by your Streamlit application (e.g., `pandas`, `numpy`, etc.).
- **Running the Streamlit application**: The command `streamlit run main.py` is used to start the Streamlit app, so Streamlit must be installed in the environment.

---

## Python Naming Conventions and Best Practices

This document outlines Python naming conventions and best practices for naming files, functions, variables, classes, and constants in Python projects. Following these conventions ensures consistency, readability, and maintainability across your codebase. The guidelines are based on **PEP 8**, the official style guide for Python code.

---

### Summary of Naming Conventions

| **Entity**         | **Naming Convention**        | **Example**                  |
|--------------------|------------------------------|------------------------------|
| **Files**          | snake_case                   | `database_connection.py`      |
| **Functions**      | snake_case()                 | `fetch_data()`                |
| **Variables**      | snake_case                   | `total_weight`                |
| **Classes**        | PascalCase                   | `UserProfile`                 |
| **Constants**      | UPPERCASE_WITH_UNDERSCORES    | `MAX_RETRIES`                 |
| **Private Methods**| _underscore_prefix()          | `_connect_to_database()`      |

---

## Setting Up Automatic Background Execution of Streamlit Apps on Windows

This section explains how to set up your Streamlit applications to run in the background automatically when your PC starts or restarts using a batch script and the Windows Task Scheduler.

### Step 1: Create a Batch Script to Run Streamlit Apps in the Background

1. Open a text editor (such as Notepad) and paste the following content:

    ```bat
    @echo off
    :: Start main.py on port 8501 in the background
    start /b "" streamlit run main.py --server.port 8501

    :: Start documentation.py on port 8504 in the background
    start /b "" streamlit run documentation.py --server.port 8504

    :: Start testPage.py on port 8503 in the background
    start /b "" streamlit run testPage.py --server.port 8503

    exit
    ```

2. Save this file as `run_streamlit_apps.bat` in a location where it will not be deleted or moved (e.g., `C:\Scripts\run_streamlit_apps.bat`).

### Step 2: Set Up Task Scheduler to Run the Script at Startup

1. Press `Win + R` to open the **Run** dialog.
2. Type `taskschd.msc` and press **Enter** to open **Task Scheduler**.

### Step 3: Create a New Task

1. In **Task Scheduler**, click **Create Task**.
2. In the **General** tab:
    - Name the task, e.g., **Run Streamlit Apps**.
    - Select **Run whether user is logged on or not**.
    - Check **Do not store password** if you want the task to run without needing a password.

### Step 4: Configure Triggers

1. In the **Triggers** tab, click **New**.
2. In the **Begin the task** dropdown, select **At startup**.
3. Click **OK** to save the trigger.

### Step 5: Configure Actions

1. In the **Actions** tab, click **New**.
2. Select **Start a program** from the **Action** dropdown.
3. In **Program/script**, click **Browse** and select the `run_streamlit_apps.bat` file created earlier.
4. Click **OK** to save the action.

### Step 6: Test the Task

1. In **Task Scheduler**, right-click on the task and select **Run** to test whether the Streamlit apps start correctly.
2. Restart your computer to confirm that the task runs automatically on startup.

By following these steps, your Streamlit apps will start running in the background automatically each time the computer starts or restarts.

---
