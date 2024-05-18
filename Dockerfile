FROM python:3.12-alpine

RUN adduser --disabled-password --gecos '' portfolio_bot
WORKDIR /opt/

COPY requirements.txt ./temp/
RUN pip install -r ./temp/requirements.txt
# Remove requirements.txt
RUN rm -rf ./temp

COPY . .
RUN chown -R portfolio_bot:portfolio_bot .
USER portfolio_bot

ENV PATH="/opt/.venv/bin:$PATH"

