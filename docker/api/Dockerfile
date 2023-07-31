FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /workspace

# poetryインストール
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc && . ~/.bashrc && poetry config virtualenvs.create false

ADD . /workspace/

# poetryで依存関係をインストール
RUN poetry install
