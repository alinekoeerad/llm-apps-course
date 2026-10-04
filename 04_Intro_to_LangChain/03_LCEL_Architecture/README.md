# LCEL Architecture ⛓️

This section introduces **LangChain Expression Language (LCEL)**. We transition from nested, manual executions to elegant, pipeline-based chains using the Pipe (`|`) syntax.

## 📝 Notebooks

1. **[01_lcel_basics.ipynb](./01_lcel_basics.ipynb)**
   - Understanding the difference between the manual execution and LCEL.
   - Building a basic chain: `Prompt | Model | OutputParser`.

2. **[02_runnable_parallel.ipynb](./02_runnable_parallel.ipynb)**
   - Using `RunnableParallel` to execute multiple chains concurrently.
   - Educational Teaser: Missing variables in parallel execution.

3. **[03_injecting_python_logic.ipynb](./03_injecting_python_logic.ipynb)**
   - Wrapping standard Python functions using `RunnableLambda`.
   - Real-world use case: Safely extracting JSON objects.

4. **[04_runnable_passthrough.ipynb](./04_runnable_passthrough.ipynb)**
   - Using `RunnablePassthrough` to preserve data through the pipeline.
   - Building a mini-RAG simulator to pass queries untouched alongside external contexts.
   - Using `.assign()` to append new data to existing dictionaries dynamically.