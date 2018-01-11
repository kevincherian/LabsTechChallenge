from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/kr2741', methods=['GET'])
def kr2741():
	return render_template('kr2741.html')

if __name__ == '__main__':
    app.run()
