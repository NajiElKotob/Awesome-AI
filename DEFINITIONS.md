# AI, ML & Generative AI – Essential Terms

## 1. Foundations

* **Artificial Intelligence (AI) – الذكاء الاصطناعي**
  - Building computer systems that do tasks normally needing human intelligence, like understanding language, recognizing images, and making decisions.
* **Data – البيانات**
  - Recorded facts, numbers, text, images, or signals that an AI system learns from and works on.
* **Dataset – مجموعة البيانات**
  - An organized collection of data used to train or test a model.
* **Algorithm – الخوارزمية**
  - A step-by-step set of instructions for doing a task, such as processing data or training a model.
* **Model – النموذج**
  - The result of training an algorithm on data; it stores learned patterns and applies them to new inputs.
* **Parameters – المعاملات**
  - The internal values (e.g., weights) a model learns during training.
* **Hyperparameters – المعاملات الفائقة**
  - Settings chosen before training (e.g., learning rate) that control how the model learns.
* **Turing Test – اختبار تورنغ**
  - A test proposed by Alan Turing (1950): if a person chatting with a machine can't reliably tell it apart from a human, the machine is said to show intelligent behavior.
 

## 2. Machine Learning

* **Machine Learning (ML) – تعلّم الآلة**
  - A way for systems to learn patterns from data instead of following hand-written rules.
* **Supervised Learning – التعلّم الخاضع للإشراف**
  - Learning from examples that include the correct answer (e.g., emails marked spam or not spam).
* **Unsupervised Learning – التعلّم غير الخاضع للإشراف**
  - Finding hidden patterns or groups in data that has no correct answers attached.
* **Reinforcement Learning – التعلّم المعزّز**
  - Learning by trial and error, where the system gets rewards or penalties for its actions.
* **Label – الوسم**
  - The correct answer attached to a training example (e.g., "fraud" or "not fraud").
* **Feature – الخاصية**
  - A single measurable attribute of the data, such as a customer's age or a pixel's brightness.
* **Feature Extraction – استخراج الخصائص**
  - Turning raw data into a smaller, more useful set of features.
* **Feature Engineering – هندسة الخصائص**
  - Selecting, combining, and reshaping features so patterns are easier for the model to detect.
* **Training – التدريب**
  - Feeding data to a model so it adjusts its parameters and learns patterns.
* **Validation – التحقق**
  - Checking the model on a separate data portion during development to tune it and compare options.
* **Testing – الاختبار**
  - Measuring final performance on data the model has never seen.
* **Prediction – التنبؤ**
  - Estimating an unknown value from known inputs.
* **Classification – التصنيف**
  - Prediction where the output is a category (e.g., approve / reject).
* **Regression – الانحدار**
  - Prediction where the output is a number (e.g., next month's sales).
* **Clustering – التجميع**
  - Grouping similar items together without predefined labels (e.g., customer segments).
* **Loss Function – دالة الخسارة**
  - A formula that measures how wrong the model's predictions are.
* **Optimization – التحسين**
  - Adjusting a model's parameters to reduce its errors (loss).
* **Gradient Descent – الانحدار التدرّجي**
  - The most common optimization method: small repeated steps in the direction that lowers the error.
* **Overfitting – فرط التلاؤم**
  - The model memorizes training data too closely and performs poorly on new data.
* **Underfitting – قصور التلاؤم**
  - The model is too simple to capture the real patterns in the data.
* **Bias – التحيّز**
  - Systematic unfairness or error in results, often caused by unbalanced or skewed training data.

## 3. Deep Learning

* **Neural Network – الشبكة العصبية**
  - A model made of connected nodes arranged in layers, loosely inspired by the brain.
* **Deep Learning – التعلّم العميق**
  - Machine learning using neural networks with many layers; powers image, speech, and language AI.
* **Transformer – المحوّل**
  - A neural network design that processes whole sequences at once; the basis of modern LLMs.
* **Attention – آلية الانتباه**
  - A technique that lets a model focus on the most relevant parts of the input when producing output.

## 4. Generative AI

* **Generative AI – الذكاء الاصطناعي التوليدي**
  - AI that creates new content – text, images, audio, code – based on patterns learned from data.
* **Large Language Model (LLM) – النموذج اللغوي الكبير**
  - A very large model trained on huge amounts of text to understand and generate language (e.g., Claude, GPT).
* **Foundation Model – النموذج الأساسي**
  - A large general-purpose model that can be adapted to many tasks.
* **Multimodal – متعدد الوسائط**
  - A model that handles more than one type of input or output, such as text and images.
* **Token – الرمز (التوكن)**
  - A small chunk of text (a word or part of a word) that an LLM reads and writes; also the unit for pricing and limits.
* **Context Window – نافذة السياق**
  - The maximum amount of text (in tokens) a model can consider at once.
* **Prompt – الموجّه**
  - The instruction or question given to a generative AI model.
* **Prompt Engineering – هندسة الأوامر**
  - Writing and structuring prompts to get accurate, useful outputs.
* **Inference – الاستدلال**
  - Using a trained model to produce an answer or output.
* **Temperature – درجة العشوائية**
  - A setting that controls how creative (high) or predictable (low) a model's output is.
* **Embedding – التمثيل المتجهي**
  - Converting text or images into lists of numbers that capture meaning, so similar items sit close together.
* **Vector Database – قاعدة البيانات المتجهية**
  - A database that stores embeddings and quickly finds items with similar meaning.
* **Retrieval-Augmented Generation (RAG) – التوليد المعزّز بالاسترجاع**
  - Fetching relevant documents first, then giving them to the LLM so its answer is grounded in your data.
* **Fine-Tuning – الضبط الدقيق**
  - Further training a pre-trained model on specific data to specialize it for a task or domain.
* **Hallucination – الهلوسة**
  - When a model produces confident but false or made-up information.
* **AI Agent – الوكيل الذكي**
  - An AI system that plans steps and uses tools (search, APIs, databases) to complete a goal on its own.
* **Guardrails – ضوابط الحماية**
  - Rules and filters that keep AI outputs safe, accurate, and within policy.

## 5. Evaluation & Responsible AI

* **Accuracy – الدقة**
  - The share of predictions the model got right.
* **Precision & Recall – الضبط والاستدعاء**
  - Precision: of the items flagged, how many were correct. Recall: of the real cases, how many were caught.
* **Explainability – قابلية التفسير**
  - The ability to understand and explain why a model made a decision.
* **Responsible AI – الذكاء الاصطناعي المسؤول**
  - Designing and using AI that is fair, transparent, secure, and respects privacy.
