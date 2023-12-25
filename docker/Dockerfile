FROM python:3.9-alpine3.13
LABEL maintainer="pipedev"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./requirements.txt /tmp/requirements.txt

# Create the ~/.config/flake8 directory and copy .flake8
RUN mkdir -p /home/django-user/.config/
COPY ./.code_quality/.flake8 /home/django-user/.config/flake8
COPY ./app /app


WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        # --no-create-home \
        --home /home/django-user \
        django-user
ENV PATH="/py/bin:$PATH"
USER django-user