from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
import requests
import os

app = Flask(__name__)

API_URL = 'http://api:8000'  # replace with your FastAPI server URL

@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')  # replace with your template

@app.route('/projects/', methods=['POST'])
def create_project():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'status': request.form['status'],
        'pdf_file': request.files['pdf_file'].read()
    }
    response = requests.post(f'{API_URL}/projects/', files=data)
    return redirect(url_for('get_projects'))

@app.route('/projects/', methods=['GET'])
def get_projects():
    response = requests.get(f'{API_URL}/projects/')
    projects = response.json()
    return render_template('projects.html', projects=projects)  # replace with your template

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    response = requests.get(f'{API_URL}/projects/{project_id}')
    project = response.json()
    return render_template('project.html', project=project)  # replace with your template


@app.route('/projects/<int:project_id>/pdf', methods=['GET'])
def get_project_pdf(project_id):
    response = requests.get(f'{API_URL}/projects/{project_id}/pdf')
    pdf_data = response.content
    response = make_response(pdf_data)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename=f'{project_id}.pdf')
    return response

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = {}
    files = {}
    if 'name' in request.form:
        data['name'] = request.form['name']
    if 'description' in request.form:
        data['description'] = request.form['description']
    if 'status' in request.form:
        data['status'] = request.form['status']
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']
        files['pdf'] = (pdf_file.filename, pdf_file)  # pass the file object directly

    response = requests.put(f'{API_URL}/projects/{project_id}', data=data, files=files)
    return jsonify(project_id=project_id)

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    response = requests.delete(f'{API_URL}/projects/{project_id}')
    if response.status_code != 200:
        return jsonify({'error': 'An error occurred'}), 500
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)