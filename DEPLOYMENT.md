# Deployment Guide: Hugging Face Spaces

Deploy your **Plant Disease AI** website online for free with **16 GB RAM** and a permanent public HTTPS link on **Hugging Face Spaces**.

---

## Prerequisites
- A free account on [huggingface.co](https://huggingface.co/join) (takes 30 seconds, no credit card required).
- Git installed on your computer.

---

## Step 1: Create a New Space on Hugging Face

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space).
2. Fill in the details:
   - **Space name**: `plant-disease-ai` (or any name you like)
   - **License**: `mit` or `openrail`
   - **Select the Space SDK**: Choose **Docker** (Blank)
   - **Space hardware**: Select **CPU basic • 2 vCPU • 16 GB RAM • FREE**
   - **Visibility**: **Public**
3. Click **Create Space**.

---

## Step 2: Get Your Hugging Face Access Token

1. Go to your Hugging Face Settings: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
2. Click **Create new token**.
3. Choose Token type: **Write**.
4. Name it (e.g., `spaces-deploy`) and copy the generated token (`hf_...`). You will use this token as your git password.

---

## Step 3: Push Your Project to Hugging Face

Open your terminal or PowerShell in your project folder (`C:\Users\Dell\Desktop\PlantDiseaseAI`):

```powershell
# 1. Commit all latest files
git add .
git commit -m "Configure Dockerfile and Hugging Face deployment"

# 2. Add Hugging Face Space as a git remote
# Replace <YOUR-USERNAME> and <YOUR-SPACE-NAME> with your actual Hugging Face details
git remote add space https://huggingface.co/spaces/<YOUR-USERNAME>/plant-disease-ai

# 3. Push to Hugging Face
git push --force space main
```

> **Note on Authentication:**
> When prompted for credentials:
> - **Username**: Your Hugging Face username
> - **Password**: Your Hugging Face Access Token (`hf_...`) generated in Step 2.

---

## Step 4: Watch it Build & Go Live!

1. Open your Space page on Hugging Face in your browser:
   `https://huggingface.co/spaces/<YOUR-USERNAME>/plant-disease-ai`
2. You will see the build logs compiling the Docker container (takes ~2-3 minutes to download TensorFlow).
3. Once the build finishes, status will switch to **Running** with a green badge.
4. Your website is now live on the internet! Anyone in the world can open:
   `https://<YOUR-USERNAME>-plant-disease-ai.hf.space`

---

## Alternative: Direct Web UI Upload (No Git CLI needed)

If you prefer uploading via your browser without using Git commands:
1. In your newly created Hugging Face Space, click the **Files** tab.
2. Click **Add file** -> **Upload files**.
3. Drag and drop:
   - `Dockerfile`
   - `requirements.txt`
   - `server.py`
   - `disease_info.py`
   - `class_names.json`
   - `README.md`
   - The `static/` folder
   - The `models/` folder (contains `plant_disease_model.keras` and `confusion_matrix.png`)
4. Click **Commit changes to main**.
5. Hugging Face will automatically build and launch your website!
