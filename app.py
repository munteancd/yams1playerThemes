from flask import Flask, render_template, request

app = Flask(__name__)

row_names = ["1", "2", "3", "4", "5", "6", "TB", "mi", "Ma", "TM", "P", "I", "1p", "2p", "3b", "F", "q", "Q", "K", "Y", "TC", "TO"]

dropdown_values = {
    "1": [0, 1, 2, 3, 4, 5],
    "2": [0, 2, 4, 6, 8, 10],
    "3": [0, 3, 6, 9, 12, 15],
    "4": [0, 4, 8, 12, 16, 20],
    "5": [0, 5, 10, 15, 20, 25],
    "6": [0, 6, 12, 18, 24, 30],
    "mi": list(range(5, 31)),
    "Ma": list(range(5, 31)),
    "P": [0, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
    "I": [0, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],
    "1p": [0, 2, 4, 6, 8, 10, 12],
    "2p": [0, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    "3b": [0, 8, 11, 14, 17, 20, 22, 23, 25, 28],
    "F": list(range(0, 49)),
    "q": [0, 30, 45],
    "Q": [0, 40, 60],
    "K": [0, 29, 33, 37, 41, 45, 49, 54, 58, 62, 66, 70, 74],
    "Y": [0, 55, 60, 65, 70, 75, 80, 105, 110, 115, 120, 125, 130]
}

@app.route('/')
def index():
    return render_template('index.html', row_names=row_names, dropdown_values=dropdown_values)

@app.route('/process', methods=['POST'])
def process():
    entries = [
        [request.form.get(f'entry_{row}_{col}', '0') for col in range(4)]
        for row in range(21)
    ]
    return render_template('result.html', entries=entries, row_names=row_names)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
