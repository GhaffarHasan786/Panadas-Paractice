# 🐼 Enterprise Data Engineering & Analysis with Pandas

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

## 📌 Executive Summary
This repository is a comprehensive showcase of **Production-Grade Data Wrangling** using the Pandas ecosystem. Moving beyond basic syntax, this project focuses on building high-throughput **ETL (Extract, Transform, Load)** pipelines. 

The core philosophy here is **Computational Efficiency**: leveraging vectorized operations to eliminate Python-level overhead and implementing memory-safe transformations for large-scale datasets.



---

## 🛠️ Toolchain & Tech Stack

To achieve high-performance data processing, the following tools and sub-libraries are utilized:

* **Pandas (Core):** For high-level data structures (Series & DataFrames).
* **NumPy (Backend):** Used for low-level vectorized array computations and linear algebra.
* **OpenPyXL / XlsxWriter:** For advanced Excel engine integration and automated reporting.
* **PyArrow / FastParquet:** To handle high-speed I/O for Parquet files (Columnar Storage).
* **Matplotlib/Seaborn:** Integrated for Exploratory Data Analysis (EDA) and distribution plotting.

---

## 🏗️ Technical Deep-Dive

### ⚡ 1. Vectorized Mapping & UFuncs
Standard loops in Python are $O(n)$. In this repository, I demonstrate how to shift computation to the C-backend of NumPy/Pandas.
* **Broadcasting:** Implementing scalar-to-vector operations that run 100x faster than `.apply()`.
* **Cython Optimization:** Utilizing internal Pandas optimizations for aggregation.

### 🧠 2. Advanced Memory Management
Handling large datasets requires more than just high RAM; it requires smart indexing.
* **Downcasting:** Converting `float64` to `float32` and `int64` to `int16` where precision allows.
* **Category Dtype:** Transforming low-cardinality string columns into `category` types to reduce memory footprint by ~80%.
* **Lazy Loading:** Implementing `chunksize` parameters for processing datasets larger than available system memory.

### 🔄 3. Relational & Temporal Logic
* **Complex Joins:** Mastering many-to-one and many-to-many merges with optimized 'on' keys.
* **Window Functions:** implementing `rolling()`, `expanding()`, and `ewm()` for statistical smoothing and trend detection.
* **Resampling:** Transforming time-series data from seconds to hourly/daily grains for high-level forecasting.

---

## 📂 Project Architecture
```text
├── 01_performance_benchmarks/  # Comparison: Loops vs Vectorization
├── 02_etl_pipelines/          # Raw data to cleaned 'Gold' tables
├── 03_time_series_forecasting/ # Lag features and rolling window logic
├── 04_memory_optimization/     # Downcasting and Category dtype tests
├── datasets/                   # Sample data (metadata & schemas only)
└── requirements.txt            # venv dependency manifest
