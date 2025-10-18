Title: Understanding AI and Large Language Models  
Date: 2025-10-17  
Category: AI Learning Journey  
Tags: ai, llm, openai, learning  
Slug: understanding-ai  
Summary: A simple introduction to how AI and large language models work — and why I decided to start learning about them during paternity leave.  

When I started learning about AI, I didn’t set out to become a researcher.
I just wanted to understand what was actually happening behind the curtain.

During my paternity leave, I’ve been using the quiet moments between feeds and naps to explore how modern AI works. I come from a finance and analytics background—my day job is about understanding how things create value. It’s hard to ignore that artificial intelligence is changing that equation faster than almost anything else.

So this post is a starting point: what AI really is, what large language models do, and why I think it matters to learn about them now.

---

## What AI Actually Is

AI, in simple terms, is about teaching computers to perform tasks that usually require human intelligence—like writing, problem solving, or recognizing patterns.

Old-school AI systems were built for narrow goals: detecting fraud, predicting churn, recommending products. But the past few years have shown that if you train models on *enough* data, they begin to generalize—to find patterns they weren’t specifically told to look for.

That’s where the current wave of “generative” AI comes from.
It doesn’t just analyze information; it produces it.

---

## What Makes a Language Model “Large”

A **large language model (LLM)** is an AI system trained on an enormous dataset of text—books, code, articles, conversations.
It doesn’t memorize facts. It learns *relationships*: how words, concepts, and meanings connect statistically.

When you prompt it with a question, it predicts the most likely next word, then the next, and so on.
That simple mechanism—predicting the next token—becomes surprisingly powerful. It allows the model to write essays, generate code, explain ideas, and even simulate reasoning.

The “large” part refers to scale: billions of parameters, trillions of training tokens, and massive compute resources.
Scale is what gives LLMs their fluency.

---

## The Two Worlds of AI

Right now, AI development splits into two main worlds:

1. **Frontier models** – built by companies like OpenAI, Anthropic, and Google. These are massive, cloud-based systems trained on industrial-scale infrastructure. They’re incredibly capable but closed-source—you access them through APIs.

2. **Open-source models** – smaller, community-built versions that can run locally on your laptop. They’re less powerful (for now) but open, flexible, and improving fast.

I’m learning from both.
The frontier models show what’s possible.
The open models show how quickly the field is democratizing.

---

## Why This Matters

AI is becoming a new kind of literacy.
You don’t need to be a software engineer to benefit—but understanding the basics helps you use it thoughtfully.

For me, learning AI isn’t about chasing hype. It’s about curiosity. About understanding the mechanics of a technology that’s going to reshape how we work, think, and create.

Even a basic grasp of how these systems operate—what an API is, what a “prompt” does—makes everything else feel less abstract. Once you understand how it talks, you can start to build things that talk back.

---

## What’s Next

In the next post, I’ll move from theory to practice—showing how to make your first API call to a model and understand what’s happening under the hood.

Here’s a preview:

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful tutor."},
        {"role": "user", "content": "Explain large language models in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

That’s all it takes to start a conversation with a model.
From there, you can ask questions, generate text, or even build your own tools.

The magic is not in the code itself—it’s in learning how to shape the conversation.


