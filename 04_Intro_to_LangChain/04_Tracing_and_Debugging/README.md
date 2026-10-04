# Tracing and Debugging 🐛🔍

In this section, we explore how to look "under the hood" of LangChain pipelines. As chains become more complex, identifying bottlenecks, errors, and token usage becomes crucial.

## 📝 Notebooks

1. **[01_tracing_and_debugging.ipynb](./01_tracing_and_debugging.ipynb)**
   - **Level 1 (Console Debugging):** Using `set_debug(True)` for rapid, verbose console logs during early development.
   - **Level 2 (Visualizing Architecture):** Using `.get_graph().print_ascii()` along with the `grandalf` library to print the architectural flow of LCEL chains.
   - **Level 3 (Professional Tracing):** Setting up environment variables to log traces, token usage, and latency metrics to the **LangSmith** dashboard.