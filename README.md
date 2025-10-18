# Quick Directions – Clone Project to Your Computer

If your teammate just needs the code locally, follow these simple steps (no SSH setup required):

---

### 1️⃣ Install prerequisites

* Make sure **Git** and **Python 3** are installed.
* Optional: install **VS Code** or **Cursor** to edit and run Python.

---

### 2️⃣ Clone the repository (get the files)

**Option A — Command line**

```bash
cd ~/Projects  # or any folder you like
git clone https://github.com/<org-or-user>/<repo>.git
cd <repo>
```

**Option B — GitHub Desktop**

1. Open GitHub Desktop → **File → Clone Repository…**
2. Paste the HTTPS URL (from the green “Code” button on GitHub)
3. Click **Clone**

---

### 3️⃣ Open the project

* If you’re using VS Code or Cursor → choose **File → Open Folder** → pick the cloned folder.

---

### 4️⃣ (Optional) Run the code

Make sure `air_quality.csv` and `uhf.csv` are inside the same folder as `project1.py`, then run:

```bash
python project1.py
```

---

That’s it. You don’t need to push anything or create branches unless asked — just clone, open, and run.
