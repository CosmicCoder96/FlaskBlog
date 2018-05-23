FROM python:3-onbuild
EXPOSE 5000
ENV FLASK_APP=blog.py
CMD ["flask", "run", "--host=0.0.0.0"]


