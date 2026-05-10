from flask import Flask, render_template, make_response
from flask_talisman import Talisman
import os

app = Flask(__name__)

# Wrap Flask app with Talisman.
# Disable HTTPS enforcement in development because the Flask dev server runs over HTTP.
if os.getenv('FLASK_ENV') == 'development':
    Talisman(app, content_security_policy=None, force_https=False)
else:
    Talisman(app, content_security_policy=None)

@app.route('/')
# create Index page
def index():
    return render_template("index.html")


# create about page
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/download/<path:file>')
def download(file):
    import boto3
    
    bucket_name = os.getenv('S3_BUCKET_NAME')
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    # Download the file from S3
    file_data = s3.get_object(Bucket=bucket_name, Key=file)['Body'].read()

    # Create a Flask response with the file data
    response = make_response(file_data)

    # Set the appropriate content type and headers for the file
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment; filename={file}'

    return response

