# 🧠 GenderEntropyBias: RealWorldQuestioning Benchmark & Evaluation

This repository accompanies the NeurIPS 2025 submission:

> **"Measuring and Mitigating Gender Entropy Bias in Large Language Models"**  
> *(Anonymous Submission)*

---

## 📌 Overview

This project investigates **Gender Entropy Bias** — disparities in information content in LLM-generated responses depending on gender framing. It includes:

- A new **benchmark dataset** of 870+ real-world, gender-attributed questions.
- **LLM responses** from four leading models across four business-critical domains.
- Quantitative evaluation using **Shannon Entropy**, **CTTR**, **Maas**.
- Judgments from **ChatGPT-4o** as an automated evaluator.
- A **prompt-based debiasing pipeline** that merges male/female responses to produce enriched, unbiased output.

---

## 🗂 Repository Structure

GenderEntropyBias/
├── data/ # Raw gendered question datasets
│ ├── Questions_Education_Recommendations.xlsx
│ ├── Questions_Health_Recommendations.xlsx
│ ├── Questions_Investment_Recommendations.xlsx
│ └── Questions_Job_Recommendations.xlsx
│
├── output/ # Raw LLM responses by domain and model
│ └── Education/
│ └── Responses_{model}.xlsx
│ └── Health/
│ └── Responses_{model}.xlsx
│ └── Investment/
│ └── Responses_{model}.xlsx
│ └── Job/
│ └── Responses_{model}.xlsx
│
├── evaluated_output/ # Evaluation outputs
│ ├── LLM-as-Judge_ChatGPT-4o_1_Iter/
│ ├── Statistical_Evaluation_1_Iter/
│ └── Variability_Analysis_50_Iter/
│
├── debiasing_data/ # Debiased responses from iterative prompting
│ └── Education/
│ └── Health/
│ └── Investment/
│ └── Job/
│ ├── Debiased_Responses_ChatGPT-3.5_FemaleFirst.xlsx
│ ├── Debiased_Responses_ChatGPT-3.5_MaleFirst.xlsx
│ └── final.xlsx
│
├── load_dataset.py # Script to load dataset (e.g. from Hugging Face)
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # This file

Copy
Edit

---

## 📊 Evaluation Methods

We evaluated entropy bias using:

- **Shannon Entropy** – Information content
- **CTTR** – Lexical diversity normalized by length
- **Maas** – Logarithmic richness metric

Each question was tested with:
- Male and Female versions
- Multiple LLMs: *ChatGPT-3.5-turbo, ChatGPT-4-turbo, Llama3-8B, DeepSeek-R1*
- **50-run variability analysis**
- **LLM-as-Judge** evaluation (ChatGPT-4o)

---

## ✅ Key Findings

- **No significant category-level bias** in entropy across LLMs.
- **Individual-level discrepancies** in response richness are common.
- **Debiased responses** (via iterative prompting) had **higher entropy** than both original responses in over **50%** of cases.

---

## 📥 Using the Dataset

The main questions are located in `data/`. Each `.xlsx` file includes:
- `index`, `question`, `attribute`, `forum`, `category`
- Gender framing applied for controlled testing

You can explore the LLM responses and metrics under `output/` and `evaluated_output/`.

---

## 📜 License

This project and dataset are released under the [**MIT License**](./LICENSE).  
You are free to use, modify, and distribute the contents with proper attribution.

---

## 📌 Citation

If you use this dataset or evaluation results in your work, please cite:

```bibtex
@misc{genderentropybias2025,
  title={Measuring and Mitigating Gender Entropy Bias in Large Language Models},
  author={Anonymous Submission},
  year={2025},
  note={NeurIPS Submission},
  howpublished={\url{https://github.com/TheAIResearcher/GenderEntropyBias}}
}
