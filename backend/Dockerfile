FROM python:3.8.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /backend
WORKDIR /backend
COPY . /backend
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8000
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "django_project.wsgi:application"]
