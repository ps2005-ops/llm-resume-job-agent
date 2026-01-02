# LLM Resume & Job Application Agent

Agent-based AI system with:
- Tool calling
- Retrieval (RAG)
- Fit scoring
- Guardrails
- Task automation

## Ingest data
```bash
python ingest/ingest.py
```

## Run locally
```bash
uvicorn api.main:app --reload
```

## Example task
```bash
curl -X POST http://127.0.0.1:8000/run \
 -H "Content-Type: application/json" \
 -d '{"task":"Generate tailored resume bullets for this job"}'
```

## Docker
```bash
docker build -t resume-agent .
docker run -p 8000:8000 resume-agent
```
