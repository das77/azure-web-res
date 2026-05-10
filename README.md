# Flask Resume Website

A small Flask application that serves a resume website with a homepage, an about page, and S3-backed resume downloads.

## Project Overview

- `app.py` is the Flask application entry point.
- The app renders a resume-style homepage from `templates/index.html`.
- An `About` page is available at `/about`.
- The `/download/<path:file>` route downloads files from an S3 bucket using `boto3`.
- `flask_talisman` is used to wrap the app for security headers, with `content_security_policy=None` configured.

## Features

- Responsive resume website layout
- Linked homepage and about page
- Resume download buttons that request files from AWS S3
- Heroku-compatible deployment via `Procfile`

## Requirements

- Python 3
- `Flask`
- `boto3`
- `flask_talisman`
- `gunicorn`

Install dependencies with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

The download route requires AWS credentials and an S3 bucket name as environment variables:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `S3_BUCKET_NAME`

Example:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export S3_BUCKET_NAME=your_bucket_name
```

## Running Locally

Use Flask's development server:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Or run with Gunicorn:

```bash
gunicorn app:app
```

## Deployment

This repository includes a `Procfile` for Heroku:

```text
web: gunicorn app:app
```

It also includes an Azure Web App deployment workflow in `.github/workflows/main_python-flask-res.yml`.

The GitHub Actions workflow deploys the app to an Azure App Service named `Python-flask-res` and uses a service principal for authentication.

Required repository secrets for Azure deployment:

- `AZUREAPPSERVICE_CLIENTID`
- `AZUREAPPSERVICE_TENANTID`
- `AZUREAPPSERVICE_SUBSCRIPTIONID`

Once those secrets are configured, pushing to `main` or manually running the workflow will deploy the app to Azure.

The app can still be deployed to any platform that supports WSGI apps and environment variables.

## Project Structure

- `app.py` - main Flask application and S3 download route
- `requirements.txt` - Python package dependencies
- `Procfile` - Gunicorn process declaration for deployment
- `runtime.txt` - Python runtime version for Heroku
- `templates/` - HTML templates for pages
- `static/` - CSS, JavaScript, and image assets

## Notes

- The site uses JavaScript in `templates/index.html` to perform AJAX downloads from the `/download/` route.
- The resume download icons request `/David_Spera-Principal_Infrastructure_Engineer.pdf` and `/David_Spera-Principal_Infrastructure_Engineer.docx` from S3.
