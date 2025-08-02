from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showcase')
def showcase():
    return render_template('showcase.html')

@app.route('/interactions')
def interactions():
    # This will be disabled/coming soon
    return render_template('coming_soon.html', section='Interactions & Animations')

@app.route('/transitions')
def transitions():
    # This will be disabled/coming soon
    return render_template('coming_soon.html', section='Transitions & Effects')

@app.route('/component/<component_name>')
def component(component_name):
    return render_template(f'components/{component_name}.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)