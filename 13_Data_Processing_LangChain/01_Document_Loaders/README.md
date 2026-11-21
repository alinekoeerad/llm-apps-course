# Document Loaders

مفاهیم پردازش اسناد، بارگذاری داده‌ها از منابع گوناگون و آناتومی کلاس `Document` در LangChain.

## Scripts & Notebooks
- [`01_document_anatomy_and_principles.ipynb`](./01_document_anatomy_and_principles.ipynb): محدودیت پنجره زمینه (Context Window) و عینک نزدیک‌بین مدل‌ها، مراحل خط لوله ETL در RAG، آناتومی کلاس `Document` (`page_content` و `metadata`)، و حل تناقض اطلاعات با فیلترینگ متادیتا.
- [`02_document_loaders_guide.ipynb`](./02_document_loaders_guide.ipynb): راهنمای جامع لودرها در LangChain: بارگذاری متون ساده با `TextLoader`، استخراج اسناد PDF چندصفحه‌ای با `PyPDFLoader` و کلید `page` در متادیتا، استخراج تمیز و هدفمند وب با `WebBaseLoader` و `SoupStrainer`، و مقایسه معماری Eager Loading در برابر Lazy Loading (`lazy_load()`) برای داده‌های کلان سازمانی.
