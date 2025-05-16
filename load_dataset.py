from datasets import load_dataset
import pandas as pd

# Load the full dataset from HuggingFace
dataset = load_dataset("TheAIResearcher/RealWorldQuestioning") 

# Convert to pandas DataFrame
# Combine all splits into one DataFrame
df = pd.concat(
    [pd.DataFrame(dataset[split]) for split in dataset],
    ignore_index=True
)
print("Columns found:", df.columns.tolist())

# Ensure the category column exists and is lowercase-insensitive
df['category'] = df['category'].str.strip().str.title()

# Define categories to split
categories = ['Education', 'Job', 'Investment', 'Health']

# Save each category to a separate CSV file
for category in categories:
    # Filter by category
    df_cat = df[df['category'] == category].copy()

    # Keep only selected columns
    df_cat = df_cat[['group_index', 'attribute', 'question', 'change']].copy()

    # Extract numeric part from 'group_index' (e.g., EM001 → 1)
    df_cat['group_index'] = df_cat['group_index'].str.extract(r'(\d+)$')[0].astype(int)

    # Rename columns
    df_cat = df_cat.rename(columns={
        'group_index': 'Index',
        'attribute': 'Attribute',
        'question': 'Question',
        'change': 'Changed'
    })

    df_cat = df_cat.sort_values(by='Index').reset_index(drop=True)

    filename = f"Questions_{category}_Recommendations.xlsx"
    df_cat.to_excel(filename, index=False)
    print(f"✅ Saved {len(df_cat)} entries to {filename}")
