FROM python:3.6 AS base
ADD /azure-vote /app
WORKDIR /app
# RUN pip install --user -r requirements.txt
RUN pip install --user redis flask==2.0.1
RUN ls /root/.local/

FROM mcr.microsoft.com/vscode/devcontainers/python:3.6 AS development
COPY --from=base /root/.local /root/.local
RUN pip install --user flake8 pytest pytest-cov autopep8 ipython

FROM tiangolo/uwsgi-nginx-flask:python3.6 AS production
COPY --from=base /root/.local /root/.local
COPY /azure-vote /app
EXPOSE 80
