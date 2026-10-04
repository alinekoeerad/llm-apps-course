# LCEL Architecture ⛓️

This section introduces **LangChain Expression Language (LCEL)**. We transition from nested, manual executions to elegant, pipeline-based chains using the Pipe (`|`) syntax.

## 📝 Notebooks

1. **[01_lcel_basics.ipynb](./01_lcel_basics.ipynb)**
   - Understanding the difference between the manual execution and LCEL.
   - Building a basic chain: `Prompt | Model | OutputParser`.
   - Using `StrOutputParser` to extract raw strings from AI Messages.
   - Swapping chain components like Lego blocks using `CommaSeparatedListOutputParser`.

2. **[02_runnable_parallel.ipynb](./02_runnable_parallel.ipynb)**
   - Using `RunnableParallel` to execute multiple chains concurrently.
   - Decreasing overall latency by running independent tasks simultaneously.
   - Combining parallel outputs into a final summary chain.
   - **Educational Teaser:** Understanding why variables get lost in parallel chains (setting the stage for `RunnablePassthrough`).