from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/query-example')
def query_example():
	language = request.args.get('language') #if key doesn't exist, returns None
	framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
	website = request.args.get('website')

	return render_template('query.html', language=language, \
										framework=framework, \
										website=website)	


@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
	if request.method == 'POST':  #this block is only entered when the form is submitted
		language = request.form.get('language')
		framework = request.form.get('framework')

		return '''<h1>The language value is: {}</h1>
				  <h1>The framework value is: {}</h1>'''.format(language, framework)

	return render_template('form.html')	


@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
	req_data = request.get_json()

	# sets 'language' to None, checks if 'language' exists in JSON object and assigns to language var
	language = None
	if 'language' in req_data:
		language = req_data['language']

	framework = req_data['framework']
	python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
	example = req_data['examples'][0] #an index is needed because of the array
	boolean_test = req_data['boolean_test']

	return render_template('json.html', language=language, \
										framework=framework, \
										python_version=python_version, \
										example=example, \
										boolean_test=boolean_test)

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='127.0.0.1')