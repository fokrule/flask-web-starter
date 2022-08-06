# Flask Web Starter Application

## Project Overview

This is a simple Flask web application designed to demonstrate fundamental web development concepts, including user authentication (login/logout) and basic page navigation. It serves as a foundational project for understanding how Flask applications are structured, how to manage user sessions, and how to deploy a Python web application.

The application includes:
* **User Authentication:** A basic login and logout system.
* **Session Management:** Uses Flask's session to track user login status.
* **Dynamic Navigation:** The navigation bar dynamically changes to show "Login" or "Logout" based on the user's session status.
* **Templating:** Utilizes Jinja2 for rendering dynamic HTML content.
* **Flash Messages:** Provides feedback to the user (e.g., successful login, logout).

## Live Demo

You can see the application live at:
[https://fokrule.pythonanywhere.com/](https://fokrule.pythonanywhere.com/)

**Note:** As this is hosted on a free tier, the application might take a few seconds to "wake up" if it hasn't been accessed recently.

## Technologies Used

* **Python 3.10+**
* **Flask:** Web framework
* **Jinja2:** Templating engine (comes with Flask)
* **HTML, CSS:** Frontend structure and styling
* **python-dotenv:** For managing environment variables locally (though handled differently on PythonAnywhere free tier)


## Setup Instructions (Local Development)

To run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [git@github.com:fokrule/flask-web-starter.git](git@github.com:fokrule/flask-web-starter.git) flask-web-starter
    cd flask-web-starter
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Create a `.env` file:**
    In the root of your `flask-web-starter` directory, create a file named `.env` and add your secret key:
    ```
    SECRET_KEY="your_long_and_random_secret_key"
    ```

6.  **Run the application:**
    ```bash
    python main.py
    ```
    The application should now be running at `http://127.0.0.1:5000/`.

## Deployment on PythonAnywhere

This application is deployed on PythonAnywhere's free tier. Here's a summary of the steps involved:

1.  **PythonAnywhere Account:** Create a free "Beginner" account on [pythonanywhere.com](https://www.pythonanywhere.com/).
2.  **Upload Code:** Upload your entire `flask-web-starter` project folder (preferably by cloning your GitHub repo in a PythonAnywhere Bash console, or by zipping and unzipping).
3.  **Virtual Environment:** Create and activate a virtual environment in a PythonAnywhere Bash console, then install dependencies using `pip install -r requirements.txt`.
4.  **Web App Configuration:**
    * Go to the "Web" tab and add a new web app (manual configuration).
    * Set the Python version to **3.10** (or whatever version you used locally).
    * Set the **Source code** path to `/home/your_username/your_project_directory/`.
    * Set the **Virtualenv** path to `/home/your_username/.virtualenvs/my-virtualenv`.
5.  **WSGI Configuration:** Edit the WSGI file (`/var/www/your_username_pythonanywhere_com_wsgi.py`) to import and create your Flask app:
    ```python
    import sys
    path = '/home/your_username/your_project_directory'
    if path not in sys.path:
        sys.path.append(path)

    from website import create_app
    application = create_app()
    ```
    **Important:** Remove any default "Hello World" WSGI code from the file.
6.  **Secret Key Handling (Free Tier Specific):** Since environment variables aren't directly supported on the free tier, the `SECRET_KEY` is hardcoded directly in the `create_app` function within `website/__init__.py` (or `main.py` if `create_app` is there).
7.  **Reload Web App:** After all changes, click the "Reload" button on the "Web" tab.

## Usage

* Navigate to the home page.
* Click "Login" to access the login form. Use `username: user` and `password: password` for a successful login.
* Once logged in, the "Login" link will change to "Logout."
* Explore the "About" and "Get Quote" pages.
* Click "Logout" to end your session.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
