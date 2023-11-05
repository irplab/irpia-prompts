# IRPIA prompt

## Deployment

### Without docker

#### Use with remote GPT (OpenAI API)

* Install dependencies

```bash
 poetry install --with gpt
```

or

```bash
pip install -r gpt-requirements.txt
```
* Provide parameters 

```bash
cp .gpt.chat.env.example .env
```

Irpia-prompt engine is set to "gpt-35-chat". Fill OPENAI_API_KEY with your OpenAI API key.

```bash
ENGINE=gpt-35-chat
OPENAI_API_KEY=sk-*************************************************
```

All OpenAI API default parameters are available en `engines.yml`configuration file : 

```yaml
gpt-35-chat:
  kw_suggestion_service_factory_module: 'app.services.llm.gpt.gpt_chat_kw_suggestion_service_factory'
  kw_suggestion_service_factory_class: 'GptChatKwSuggestionServiceFactory'
  defaults:
    model_name_or_path: 'gpt-3.5-turbo'
    temperature: 0
    kw_suggestion_min_nb: 1
    kw_suggestion_max_nb: 10
```

They can be overriden in .env file. For example, to set temperature to 0.5 :

```bash
TEMPERATURE=0.5
```
To use "gpt-35-completion" with custom fine-tuned GPT model, fil OPENAI_KW_GPT_SUGGESTION_MODEL with your model name. 
As this name may differ from one user to another, it is not set in YAML configuration file.

* Launch application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```


#### Use with local LLM

* Install dependencies

```bash
poetry install --with llm
```

or

```bash
pip install -r llm-requirements.txt
```

* Provide parameters 

```bash
cp .vigogne.instruct.env.example .env
```

or
```bash
cp .vigogne.chat.env.example .env
```

Irpia-prompt engine will be set to "vigogne-instruct" or "vigogne-chat".
All default parameters from `engines.yml`configuration file can be overriden in .env file in the same way as for GPT option.

* Launch application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### With docker

#### Use with remote GPT (OpenAI API)

Run the provided image with your OpenAI API key :

```bash
docker run -d --name irpia-prompt-gpt -p 8000:8000 -e OPENAI_API_KEY=sk-************************************************* joadorn/irpia-prompt-gpt
```

#### Use with local LLM

Run the provided image on a server powered by a GPU with NVIDIA drivers installed :

```bash
docker run -d --gpus all --name irpia-prompt-llm -p 8000:8000 joadorn/irpia-prompt-llm
```

## Development

### Use with remote GPT (OpenAI API)

Generate requirements file with Openai dependencies :

```bash
poetry export --without=development,llm --with=gpt -f requirements.txt --output gpt-requirements.txt
```

Build image with this requirements :

```bash
 docker image build -t irpia-prompt-gpt:xx -f GPT-Dockerfile .
```

### Use with local LLM

Generate requirements file with LLM dependencies :


```bash
poetry export --without=development,gpt --with=llm -f requirements.txt --output llm-requirements.txt 
```

Build image with this requirements :

```bash
 docker image build -t irpia-prompt-llm:xx -f LLM-Dockerfile .
```

