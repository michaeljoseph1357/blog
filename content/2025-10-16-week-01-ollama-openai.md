Title: Week 1 — Local LLMs: Ollama vs OpenAI SDK
Date: 2025-10-16
Tags: LLMs, SDK, Python
Summary: Comparing local vs hosted models with the same client code.

Goal: talk to a local model (Ollama) *and* a hosted model using one OpenAI-style client.

**What worked**
- Keep prompts tiny and specific
- Match temperature/top_p for fairness
- Log token counts, not vibes

**Snippet**
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
resp = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role":"user","content":"3 bullets on what I learned today"}],
    temperature=0.3,
)
print(resp.choices[0].message.content)
```
