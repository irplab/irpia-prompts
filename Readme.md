_# IRPIA prompt

## Deployment

### Use with remote GPT (OpenAI API)

Install dependencies

```bash
 poetry install --with gpt
```

Generate requirements file with Openai dependencies

```bash
poetry export --without=development,llm --with=gpt -f requirements.txt --output gpt-requirements.txt
```

Build image with this requirements

```bash
 docker image build --no-cache -t irpia-prompt:xx -f LLM-Dockerfile .
```

### Use with local LLM

Install dependencies

```bash
poetry install --with llm

```

Generate requirements file

```bash
poetry export --without=development,gpt --with=llm -f requirements.txt --output llm-requirements.txt 
```

Build image with this requirements

```bash
 docker image build --no-cache -t irpia-prompt:xx -f LLM-Dockerfile .
```