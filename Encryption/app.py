from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Dictionary of valid keys mapped to their respective file URLs
KEY_FILE_URLS = {
    "cdhiouvdwjjipedvnihievjpodjip": "https://drive.google.com/file/d/1eyYaDT_HG9xIgXJxcdxPmWwd98xvW10v/view?usp=sharing",
    "4b2ab4e101ca87f70b83258d08a68ef9f74ca06df251362832127e2b18334083": "https://drive.google.com/file/d/1tfDD-HADnwwQSTVkobnYFvptmZ1Ccv8b/view?usp=sharing",
    "66b28eb656cbc1a443d245cddb4501ce26a584150bf5021699dacb0ee7cb0f19": "https://drive.google.com/file/d/1kZjGJHiYSzum-mQG5mkx13eI6CF6qmUW/view?usp=sharing",
    "053929a923501a33b9ba1978307174fd33c66a8fced55693c54ed87e38878ef6": "https://drive.google.com/file/d/1KOK_18dNeSqzJq_mI4d57I3-IM2smytr/view?usp=sharing",
    "4abf4363a2f615fb11901d9eaa4571a5bb762155e9c4aadb9cff08bcf3859e56": "https://drive.google.com/file/d/1kZjGJHiYSzum-mQG5mkx13eI6CF6qmUW/view?usp=sharing",
    "f208a14d215652816e5ceebbf0d17e1bf63ba663992b289cc509b8a6ec984aac": "https://drive.google.com/file/d/19Bx0ZGdzw7vGzW3Y8QSQLsvivcqeHaX2/view?usp=sharing",
    "e730917896243597abb68552867d25ef38b72229a684ce5d439a4aecc53abc51": "https://drive.google.com/file/d/1mG6hwV4mmuoVBNhsO4W_iNksCem4uxmU/view?usp=sharing"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify_key')
def verify_key():
    user_key = request.args.get('key')
    file_url = KEY_FILE_URLS.get(user_key)
    if file_url:
        return redirect(file_url)
    else:
        return render_template('error.html')

@app.route('/download_file')
def download_file():
    return redirect(FILE_URL)

if __name__ == '__main__':
    app.run(debug=True)
