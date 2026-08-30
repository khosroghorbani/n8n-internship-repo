You must format your output as a JSON value that adheres to a given "JSON Schema" instance.

"JSON Schema" is a declarative language that allows you to annotate and validate JSON documents.

For example, the example "JSON Schema" instance {{"properties": {{"foo": {{"description": "a list of test words", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}}} 
would match an object with one required property, "foo". The "type" property specifies "foo" must be an "array", and the "description" property semantically describes it as "a list of test words". The items within "foo" must be strings.
Thus, the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of this example "JSON Schema". The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Your output will be parsed and type-checked according to the provided schema instance, so make sure all fields in your output match the schema exactly and there are no trailing commas!

Here is the JSON Schema instance your output must adhere to. Include the enclosing markdown codeblock:
```json
{"type":"object","properties":{"output":{"type":"object","properties":{"file_content":{"type":"string"},"report":{"type":"string"}},"required":["file_content","report"],"additionalProperties":false}},"required":["output"],"additionalProperties":false,"$schema":"http://json-schema.org/draft-07/schema#"}
```

## نصب

1. مخزن را کلون کنید:

```bash
git clone <repository-url>
cd <repo-dir>
```

2. وابستگی‌ها را نصب کنید (نمونه برای پایتون):

```bash
pip install -r requirements.txt
```

یا برای Node.js:

```bash
npm install
```

3. اجرای برنامه (مثال):

```bash
python main.py
# یا
npm start
```

راهنما: مقادیر درون <> را با آدرس مخزن و مسیر واقعی پروژه جایگزین کنید. این بخش کوتاه است و می‌توانید بسته به چارچوب پروژه دستورات دقیق‌تری اضافه کنید.
