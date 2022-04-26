# import generator
# import reporter
import re
from flask import render_template
from flask import send_file
from project import app, config
from project.modules import generator, reporter


@app.route('/')
def home():
    """Serve homepage template."""
    return render_template("index.html", data={"generated": False})

@app.route('/download')
def download():
    return send_file(config.file.file_name, as_attachment=True)

@app.route('/generate')
def generate():
    response = generator.generate_data()
    
    return response


@app.route('/report')
def report():
    result = reporter.generate_report()
    
    return result

