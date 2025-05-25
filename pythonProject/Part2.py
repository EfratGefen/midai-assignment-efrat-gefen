import os
from openai import OpenAI

# 1. Set your API key directly in the code
client = OpenAI(api_key="ks-...")#dont let me uploud the code ti GIT

# 2. Read the construction specification from file
with open("construction_spec.txt", "r", encoding="utf-8") as f:
    spec_text = f.read()

# 3. Build the prompt for ChatGPT
prompt = f"""
The following text contains building specification sections.

For each paragraph, extract the following structured data:
- Element name (e.g., Wall Type A, Floor Slab B)
- Material(s)
- Thickness or dimensions
- Insulation or core material (if any)
- Finish (if mentioned)
- Structural or performance data (e.g., fire rating, load capacity, U-value)
- Intended use
- Standard or compliance code

Return only valid JSON, with one JSON object per section (paragraph).
Each object should include all fields even if some are null.
Respond with a JSON array of objects and no explanations.

Text:
\"\"\"
{spec_text}
\"\"\"
"""

# 4. Send request to OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that extracts structured data from construction specifications."},
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

# 5. Extract output
output_text = response.choices[0].message.content.strip()

# 6. Create output folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# 7. Save output to JSON file
with open("results/specifications.json", "w", encoding="utf-8") as f:
    f.write(output_text)

print("The file 'specifications.json' has been saved successfully in the 'results' folder.")
