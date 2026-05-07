import pandas as pd
import subprocess
import os

# ===== ĐƯỜNG DẪN FILE EXCEL =====
excel_file = r"C:\Users\hi\Documents\GitHub\NTH\data.xlsx"

print("🔄 Reading Excel...")

# ===== ĐỌC EXCEL =====
# chỉ lấy 2 cột đầu tiên
df = pd.read_excel(
    excel_file,
    usecols=[0, 1],
    dtype=str
)

# đổi tên cột
df.columns = ["code", "url"]

# xóa dòng trống
df = df.dropna()

# ===== XUẤT JSON =====
json_file = r"C:\Users\hi\Documents\GitHub\NTH\data.json"

df.to_json(
    json_file,
    orient="records",
    force_ascii=False,
    indent=2
)

print("✅ data.json updated!")

# ===== GIT AUTO PUSH =====
repo_path = r"C:\Users\hi\Documents\GitHub\NTH"

os.chdir(repo_path)

# pull
subprocess.run(["git", "pull"], check=True)

# add
subprocess.run(["git", "add", "."], check=True)

# commit
subprocess.run(
    ["git", "commit", "-m", "auto update"],
    check=False
)

# push
subprocess.run(["git", "push"], check=True)

print("🚀 GitHub Pages updated!")