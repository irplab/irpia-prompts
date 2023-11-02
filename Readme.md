_# IRPIA prompt

## Installation

### Use with remote GPT (OpenAI API)

Generate requirements file
```bash
poetry export --without=development,llm --with=gpt -f requirements.txt --output gpt-requirements.txt
```

### Use with local LLM

Generate requirements file
```bash
poetry export --without=development,gpt --with=llm -f requirements.txt --output llm-requirements.txt 
```

