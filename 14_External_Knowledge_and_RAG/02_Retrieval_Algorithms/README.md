# بخش ۲: الگوریتم‌های بازیابی (Retrieval Algorithms)

این پوشه شامل درسنامه‌ها، پروژه‌ها و پیاده‌سازی‌های عملی استراتژی‌های پیشرفته بازیابی اطلاعات در خطوط لوله RAG است.

---

## 🗂️ فهرست درسنامه‌ها و نت‌بوک‌ها

### ۱. [01_mmr_and_retrieval_strategies.ipynb](file:///d:/Project/LLM/llm-apps-course/14_External_Knowledge_and_RAG/02_Retrieval_Algorithms/01_mmr_and_retrieval_strategies.ipynb)
* **مفاهیم اصلی:**
  * معضل افزونگی (Redundancy) و اشباع کانتکست با چانک‌های تکراری در `Similarity Search`.
  * تشبیه شهودی تیم فوتبال (۱۱ دروازه‌بان در برابر تیم متعادل).
  * الگوریتم **MMR (Maximal Marginal Relevance)** برای ایجاد توازن پویا میان ارتباط (`Relevance`) و تنوع (`Diversity`).
  * تنظیم پارامترهای `fetch_k`, `k` و ضریب تعادل `lambda_mult` (مقایسه 1.0 و 0.5 و 0.0).
  * دفاع در برابر سوالات پرت و توهم (Hallucination) با فیلتر آستانه شباهت (`similarity_score_threshold`).
  * پیاده‌سازی زنجیره کامل LCEL با استفاده از مدل **Google Gemini** (`gemini-flash-lite-latest`).
  * ماتریس تصمیم‌گیری (Decision Matrix) برای انتخاب بهترین استراتژی بازیابی.

---

### ۲. [02_self_querying_retrieval.ipynb](file:///d:/Project/LLM/llm-apps-course/14_External_Knowledge_and_RAG/02_Retrieval_Algorithms/02_self_querying_retrieval.ipynb)
* **مفاهیم اصلی:**
  * محدودیت‌های اساسی جستجوی برداری معنایی در درک شروط دقیق، فیلترهای منطقی و مقایسه‌های ریاضی (`>`, `<`, `==`).
  * معماری **بازیابی با خود-کوئری (Self-Querying Retriever)**: استفاده از مدل زبانی به عنوان مترجم ورودی کاربر به کوئری ساختاریافته (تفکیک به Semantic Query + Metadata Filter).
  * کاتالوگ متادیتا با **`AttributeInfo`** جهت معرفی اسکیما و ستون‌های دیتابیس به LLM.
  * استفاده از **`ChromaTranslator`** برای ترجمه فیلترهای انتزاعی به ساختار استاندارد کوئری کروما.
  * سناریوی عملی کاتالوگ فیلم‌ها: استخراج فیلترهای ترکیبی (مثل `rating > 8.5` یا `genre == 'animated' and year < 2000`).
  * مقایسه عینی نقص جستجوی شباهت ساده با خود-کوئری.
  * ساخت خط لوله کامل پرسش و پاسخ RAG با تلفیق `SelfQueryRetriever` و مدل جمنای (`gemini-flash-lite-latest`).
  * جدول تحلیل مصالحه (Trade-offs: دقت، تاخیر زمانی، وابستگی به اسکیما و هزینه).
