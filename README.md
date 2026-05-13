Patient Segmentation Using K-Means Clustering

Unsupervised machine learning to identify distinct mental health patient profiles using PHQ/GAD scores and demographic features.

🔗 Live Demo

👉https://anurag-clustering-patient-segments.streamlit.app/

📌 Project Overview

This project applies K-Means clustering to segment university student patients into meaningful mental health profiles. By combining clinical PHQ/GAD scores with demographic features, the model identifies 6 distinct patient groups - ranging from low-risk healthy individuals to high-risk patients requiring urgent clinical attention.

🎯 Objectives

Apply K-Means clustering on PHQ/GAD and demographic features

Identify 4–6 distinct patient clusters with clinical interpretability

Evaluate cluster quality using silhouette score

Generate actionable patient profiles to support mental health decision-making



📁 Project Structure
📦 patient-clustering
 ┣ 📓 Cluster.ipynb                  # Main analysis notebook
 ┣ 📄 depression_anxiety_data.csv    # Raw dataset (783 rows, 19 cols)
 ┣ 📄 clustered_patients.csv         # Output: 775 patients with cluster labels
 ┣ 📄 cluster_profiles.csv           # Output: Mean profile per cluster
 ┣ 📄 Patient_Segmentation_Report.docx  # Full written report
 ┣ 📄 app.py                         # Streamlit dashboard
 ┗ 📄 README.md

🗂️ Dataset

PropertyValueSourcedepression_anxiety_data.csvTotal records783 patientsTotal columns19After preprocessing775 rows × 6 featuresMissing values8 rows dropped (epworth_score)

⚙️ Features Used for Clustering

Feature Type Description phq_score ClinicalPHQ depression scalegad_score, ClinicalGAD anxiety scale,age,Demographic Patient age,bmi,Physiologica0l,Body Mass Indexepworth_scoreSleepDaytime sleepiness scalegenderDemographicEncoded (male=0, female=1)

🔬 Methodology
Load Dataset → Feature Selection → Drop Nulls → Encode Gender
     → StandardScaler → Elbow Method → Silhouette Score
          → K-Means (k=6) → Cluster Profiles → Export CSV
Silhouette Scores (k = 4–6)
K Silhouette Score 0.2014 Best


📊 Key Findings

6 distinct patient profiles identified from 775 patients

Cluster 4 is the most critical — PHQ 17.17 & GAD 16.15 (Severe)

Cluster 2 is the largest at-risk group (167 patients, moderate symptoms

BMI is a key differentiator — Cluster 1 has mean BMI of 31.34

Gender strongly separates clusters — C0 is 100% female, C5 is 98% male

Epworth score correlates with severity — Cluster 4 scores 13.13



🛠️ Tech Stack

Tool Purpose Python Core language Pandas & NumPy ,Data manipulation ,Scikit-Learn K-Means clustering, scaling, silhouette score,Matplotlib & Seaborn Visualizations ,Streamlit, Interactive dashboard

📝 Report

A full written report is available in Anurag_Clustering_patient_segmentation.pdf

Methodology

Cluster profiles with clinical interpretation


Author
Anurag
