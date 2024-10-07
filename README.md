## Overview

The **Infeed700** application is an interactive platform developed by **ICMC Solutions** using **Streamlit**. It provides embedded dashboards and **SSRS** (SQL Server Reporting Services) reports, allowing users to access and visualize data efficiently in an on-premises environment. This application is designed to serve multiple clients, offering a user-friendly and responsive interface.

## Installation Instructions

Follow these steps to set up the **Infeed700** application on your local machine:

1. **Download Python**:
   - Visit the official Python website: [**Download Python**](https://www.python.org/downloads/)
   - Download the latest version of **Python** (make sure to choose the installer compatible with your operating system).
   - Run the installer and make sure to check the box that says **"Add Python to PATH"** during installation.

2. **Download and Extract the Application Files**:
   - Download the **Infeed700** application files, which are provided as a `.zip` or `.rar` archive.
   - Extract the contents of the archive to a local directory of your choice.

3. **Navigate to the Application Directory**:
   - Open a **command prompt** window (you can do this by searching for **"cmd"** in the Windows search bar).
   - Use the `cd` command to change to the directory where you extracted the application files. For example:
     ```
     cd path\to\your\extracted\folder
     ```

4. **Run the Setup Batch File**:
   - In the **command prompt**, execute the `setup.bat` file by typing:
     ```
     setup.bat
     ```
   - This will install all the required dependencies and start the **Streamlit** application.

5. **Access the Application**:
   - After running the setup, the **Streamlit** application should automatically launch in your web browser. If it doesn't, you can manually open your browser and go to `http://localhost:8501`.

By following these steps, you will have the **Infeed700** application set up and running on your local machine. If you encounter any issues, please refer to the troubleshooting section of this documentation or seek assistance from your IT support team.

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

#### Guidelines:
- Keep filenames short, descriptive, and to the point.
- Avoid using overly generic filenames like **file.py** or **temp.py**.

---

### 2. Naming Functions

Function names should follow the **snake_case** convention. They should be descriptive enough to clearly convey the purpose of the function.

#### Examples:
- `get_user_data()`
- `calculate_total_weight()`
- `send_email_notification()`

#### Guidelines:
- Use verbs to indicate actions: **fetch**, **load**, **process**, **calculate**.
- Avoid single-letter names like `f()` unless in very limited contexts like lambda functions.

---

### 3. Naming Variables

Variable names should also follow the **snake_case** convention and be descriptive. Short, concise names that convey meaning are ideal.

#### Examples:
- `total_weight`
- `max_date`
- `is_active_user`

#### Guidelines:
- Avoid overly generic names like **data**, **value**, **x**, etc.
- Use clear and descriptive names to improve readability.

---

### 4. Naming Classes

Class names should follow the **PascalCase** convention (also known as **CamelCase**), with the first letter of each word capitalized.

#### Examples:
- `UserProfile`
- `ReportGenerator`
- `DatabaseConnection`

#### Guidelines:
- Classes represent objects or entities, so the names should typically be nouns.
- Avoid abbreviations or short names like **UsrPrfl**. Be explicit.

---

### 5. Naming Constants

Constants should be written in **UPPERCASE** with words separated by underscores (`_`). Constants are values that should not change throughout the program.

#### Examples:
- `MAX_RETRIES`
- `DEFAULT_TIMEOUT`
- `API_KEY`

#### Guidelines:
- Use constants for configuration values, timeouts, default parameters, and other fixed values.
- Keep the constant names descriptive and meaningful.

---

### 6. Private Methods and Variables

Private methods and variables should start with a single underscore (`_`). This indicates that the method or variable is intended for internal use within the class and should not be accessed outside.

#### Examples:
- `_connect_to_database()`
- `_validate_user_input()`

#### Guidelines:
- Use private methods for functionality that should not be exposed outside the class.
- Avoid making everything private unless necessary; keep interfaces clean and intuitive.

---

### 7. Naming Test Files and Functions

When writing tests, the test file names should be in **snake_case**, typically prefixed with `test_`. Test functions should also follow **snake_case** and be descriptive.

#### Examples:
- `test_database_connection.py`
- `test_user_authentication.py`

#### Guidelines:
- Name your test functions to reflect what you are testing: `test_load_user_data()`, `test_calculate_total()`.

---

### 8. General Guidelines

- **Be descriptive**: Choose names that clearly describe the purpose of the file, function, variable, or class.
- **Avoid abbreviations**: Use full words whenever possible to make your code easier to read.
- **Keep names short but meaningful**: While names should be descriptive, avoid making them unnecessarily long.



By adhering to these naming conventions and best practices, your Python code will be more organized, easier to understand, and maintainable. Consistency is key to writing high-quality code that others (or you) can read and maintain over time.
