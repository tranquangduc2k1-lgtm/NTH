import pandas as pd
import os

# ===== PATH =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

excel_file = os.path.join(BASE_DIR, "data.xlsx")

json_file = os.path.join(BASE_DIR, "data.json")

print("🔄 Reading Excel...")

# ===== READ EXCEL =====
df = pd.read_excel(excel_file)

# ===== COLUMN =====
df.columns = ["code", "url"]

# ===== CLEAN =====
df["code"] = (
    df["code"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["url"] = (
    df["url"]
    .astype(str)
    .str.strip()
)

# ===== REMOVE EMPTY =====
df = df[df["code"] != ""]

# ===== REMOVE DUPLICATE =====
df = df.drop_duplicates(subset="code")

# ===== EXPORT JSON =====
df.to_json(
    json_file,
    orient="records",
    force_ascii=False,
    indent=2
)

print("✅ data.json updated!")

input("Press Enter to exit...")

import subprocess
import os

# thư mục project github
repo_path = r"C:\Users\hi\Documents\GitHub\NTH"

# chuyển vào thư mục
os.chdir(repo_path)

# git add
subprocess.run(["git", "add", "."])

# commit
subprocess.run(["git", "commit", "-m", "auto update"])

# push
subprocess.run(["git", "push"])