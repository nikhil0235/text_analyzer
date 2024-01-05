Text Analyzer Web App
Overview
This is a basic web application designed to analyze the text provided in a text file. The application counts the occurrences of each word in the document and presents the results on the user interface.

Features
User-friendly UI for file upload.
Authentication for basic security.
Backend processing to analyze the uploaded text file.
Display of word count results on the UI.
Technology Used
Backend: Python (Django)
Frontend: HTML, CSS
Authentication: Django Authentication System


![Screenshot 2024-01-04 150632](https://github.com/nikhil0235/text_analyzer/assets/109364387/e0e009e1-e0ae-4140-8dd6-bb6ca479aedb)
![Screenshot 2024-01-04 092735](https://github.com/nikhil0235/text_analyzer/assets/109364387/ffe5709b-e393-4f67-9bb2-d204da90cb6d)
![Screenshot 2024-01-04 150707](https://github.com/nikhil0235/text_analyzer/assets/109364387/8471e697-55d0-4435-a7e3-297140236d50)
![Screenshot 2024-01-04 150652](https://github.com/nikhil0235/text_analyzer/assets/109364387/9fc67ea6-f8b6-4af8-84e5-9f7383595221)

Assumptions
The text file provided will contain words separated by spaces.
The application assumes a single user for simplicity.
Setup Instructions
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/text-analyzer-web-app.git
Install the necessary dependencies. If you're using Django, you can do this with:

bash
Copy code
pip install -r requirements.txt
Run the Django development server:

bash
Copy code
python manage.py runserver
Visit [http://127.0.0.1:8000/analyzer/analyze] in your web browser.

You'll be prompted to log in. If you don't have an account, you can sign up.

Once logged in, navigate to the "Analyze Text" section.

Upload a text file using the provided form.

The application will process the file, and the word count results will be displayed on the UI.

Contributions
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

Issues
If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.


