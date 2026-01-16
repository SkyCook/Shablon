from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('ex1_ind.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)