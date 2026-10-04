# Models and Helpers 🤖

In this section, we explore the basics of initializing models and using helper functions in LangChain.

## 📝 Notebooks

1. **[01_simple_model.ipynb](./01_simple_model.ipynb)**
   - Initializing Google Gemini via LangChain.
   - Using the standard `.invoke()` method.
   - Extracting token usage metadata.

2. **[02_batch_and_stream.ipynb](./02_batch_and_stream.ipynb)**
   - Processing multiple conversations concurrently using `.batch()`.
   - Streaming responses token-by-token using `.stream()`.
   - Custom RTL (Right-to-Left) Markdown rendering for Persian text using `IPython.display`.