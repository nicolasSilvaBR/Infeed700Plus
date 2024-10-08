# Infeed700 Application Documentation

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

### 1. Naming Python Files

Python filenames should be written in **snake_case**, with lowercase letters and words separated by underscores (`_`). This ensures clarity and consistency.

#### Examples:
- `main.py`
- `database_connection.py`
- `report_generator.py`

---

### 2. Naming Functions

Function names should follow the **snake_case** convention. They should be descriptive enough to clearly convey the purpose of the function.

#### Examples:
- `get_user_data()`
- `calculate_total_weight()`
- `send_email_notification()`

---

### 3. Naming Variables

Variable names should also follow the **snake_case** convention and be descriptive. Short, concise names that convey meaning are ideal.

#### Examples:
- `total_weight`
- `max_date`
- `is_active_user`

---

### 4. Naming Classes

Class names should follow the **PascalCase** convention (also known as **CamelCase**), with the first letter of each word capitalized.

#### Examples:
- `UserProfile`
- `ReportGenerator`
- `DatabaseConnection`

---

### 5. Naming Constants

Constants should be written in **UPPERCASE** with words separated by underscores (`_`). Constants are values that should not change throughout the program.

#### Examples:
- `MAX_RETRIES`
- `DEFAULT_TIMEOUT`
- `API_KEY`

---

### 6. Private Methods and Variables

Private methods and variables should start with a single underscore (`_`). This indicates that the method or variable is intended for internal use within the class and should not be accessed outside.

#### Examples:
- `_connect_to_database()`
- `_validate_user_input()`

---

### 7. Naming Test Files and Functions

When writing tests, the test file names should be in **snake_case**, typically prefixed with `test_`. Test functions should also follow **snake_case** and be descriptive.

#### Examples:
- `test_database_connection.py`
- `test_user_authentication.py`

---

### 8. General Guidelines

- **Be descriptive**: Choose names that clearly describe the purpose of the file, function, variable, or class.
- **Avoid abbreviations**: Use full words whenever possible to make your code easier to read.
- **Keep names short but meaningful**: While names should be descriptive, avoid making them unnecessarily long.

---

By adhering to these naming conventions and best practices, your Python code will be more organized, easier to understand, and maintainable. Consistency is key to writing high-quality code that others (or you) can read and maintain over time.
