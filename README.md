-->> Project Title

Google Form Auto Fill using Python & Selenium

-->> About This Project

This project is a simple Python script that automatically fills a Google Form using Selenium.
It opens the Chrome browser, fills in all the form fields (like Full Name, Contact Number, Email, etc.), and then submits the form.

I used WebDriverWait so that the script waits for each field to load properly before typing anything.
This makes the automation smooth and prevents errors if the form loads slowly.

-->> How It Works

The script opens Chrome and goes to the Google Form link.

It finds each question by its label text (for example: “Full Name”, “Email ID”).

It types the answers automatically.

Finally, it clicks the “Submit” button and closes the browser.

🪜 

-->>>>Steps to Run

***   Create a new folder for the project and save your file as fill_form.py.

***   Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate


***   Install Selenium:

pip install selenium


***   Set up ChromeDriver:

Download ChromeDriver that matches your Chrome version.

Keep it in your project folder or add it to your system PATH.

***   Run the script:

python fill_form.py


***   The script will open the form, fill all the fields, and submit it automatically ✅


--->>>Files in This Project

***  fill_form.py → The main Python script.

***  requirements.txt → List of required modules (only Selenium).

***  README.md → This documentation.

***   .gitignore → To ignore unnecessary files (like venv, cache, etc.).
