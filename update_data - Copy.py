import pandas as pd
import json
import subprocess
import os

# đường dẫn file excel
excel_file = r"C:\Users\hi\Documents\GitHub\NTH\data.xlsx"

print("🔄 Reading Excel...")

# chỉ lấy 2 cột đầu tiên
df = pd.read_excel(excel_file, usecols=[0, 1])

# đổi tên cột
df.columns = ["code", "url"]

# xóa dòng trống
df = df.dropna()

# xuất json
json_file = r"C:\Users\hi\Documents\GitHub\NTH\data.json"

df.to_json(json_file, orient="records", force_ascii=False)

print("✅ data.json updated!")

# ===== GIT AUTO PUSH =====

repo_path = r"C:\Users\hi\Documents\GitHub\NTH"

os.chdir(repo_path)

subprocess.run(["git", "pull"])

subprocess.run(["git", "add", "."])

subprocess.run(["git", "commit", "-m", "auto update"])

subprocess.run(["git", "push"])

print("🚀 GitHub Pages updated!")