# LCEL Architecture ⛓️

This section introduces **LangChain Expression Language (LCEL)**. We transition from nested, manual executions to elegant, pipeline-based chains using the Pipe (`|`) syntax.

## 📝 Notebooks

1. **[01_lcel_basics.ipynb](./01_lcel_basics.ipynb)**
   - Understanding the difference between the manual execution and LCEL.
   - Building a basic chain: `Prompt | Model | OutputParser`.
   - Using `StrOutputParser` to extract raw strings from AI Messages.
   - Swapping chain components like Lego blocks using `CommaSeparatedListOutputParser` to return Python lists instead of strings.