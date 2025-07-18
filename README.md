# LLM Comparison on Tree Data

This project is dedicated to a simple benchmark for models available through the [OpenRouter](https://openrouter.ai/) API, such as:

- `moonshotai/kimi-k2:free`
- `google/gemma-2-9b-it:free`
- `anthropic/claude-sonnet-4`
- and others

### The Idea

The idea of this project is quite simple:

- First, we generate a random tree with `tree_size` nodes and no more than `density` children per node. The number of children is distributed uniformly from 1 to `density`.

- Given the tree structure, we generate a **text description** of the tree—basically, an explanation of the connections between nodes.

- Then, we generate a **query** that can be answered algorithmically. For example:
  - How many generations are present in the tree (i.e., the depth)?
  - Who is the lowest common ancestor (LCA) of two nodes?

In this setup, we have:
- a tree described in text,
- a query in text,
- and the correct answer.

We ask the model to answer the query, then:
- investigate how different parameters impact the error rate,
- and compare performance across different models.

---

The goal is to understand the current limitations of **hierarchical information extraction** from text by language models, and to identify which parameters are crucial.

This project is partially inspired by the paper  
**_"Let Your Graph Do the Talking: Encoding Structured Data for LLMs"_**,  
but our project takes a simpler, reverse perspective:

> What if the data is already in natural language, but implicitly contains hierarchical (tree-like) structure—and we have no resources to parse it back into structured form or fine-tune an encoder? Can LLMs still reason about such structure purely from text?

### Installation
This project uses [Poetry](https://python-poetry.org/) for dependency management. To install:
```bash
poetry install
```

### Project Structure
`llm_comparison/generators.py` — logic for generating random trees, textual descriptions, and queries.
`data` — folder to collect the data for queries generation and models benchmarks data.
`notebooks/comparison.ipynb` — main notebook with benchmarks and analysis.

### Contacts
Anton: [eliseevantoncoon@gmail.com](mailto:eliseevantoncoon@gmail.com)  
PRs are very welcome — have fun!
