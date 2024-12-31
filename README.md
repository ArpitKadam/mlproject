# 🌟 Students Performance Prediction

## 🌐 Demo
🔗 [Live Demo](https://mlproject-kyw0.onrender.com)

## 📖 Overview
This project is designed to provide insights and predictions using a comprehensive pipeline for data processing, analysis, and visualization. The repository includes components for web interaction, machine learning pipelines, and detailed visualizations to explore data trends and patterns.

## ✨ Features
- 📊 **Data Analysis and Visualization**: Prebuilt plots in the `Visualization_images` directory showcase key data trends.
- 🤖 **Machine Learning Pipelines**: Scripts for training and prediction workflows are available in the `/src` directory.
- 🌐 **Web Interface**: A simple HTML interface is included in the `templates` directory.
- 🐳 **Containerization**: Docker support for seamless deployment.

## 🗂️ Directory Structure
```
/                           # Root directory
|-- artifacts/              # Models, Test and Train data
|-- logs/                   # Logs of project
|-- data/                   # Datasets
|-- mlproject.egg-info/     # Whole project avaliable as a package      
|-- notebook/               # Jupyter notebooks
|-- LICENSE                 # License file
|-- README.md               # Project documentation
|-- requirements.txt        # Python dependencies
|-- Visualization_images/   # Plots and visualizations
|-- templates/              # HTML templates for the web interface
|-- src/                    # Source code
|   |-- components/         # Modular components for tasks
|   |-- pipeline/           # Training and prediction pipelines
|   |-- utils.py            # Utility functions
|-- Dockerfile              # Docker configuration
|-- app.py                  # Main application script
|-- setup.py                # Package setup file
```

## 🚀 Getting Started

### ✅ Prerequisites
- 🐍 Python 3.8+
- 🐳 Docker (optional, for containerized deployment)

### 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the Application
To start the application locally:
```bash
python app.py
```

### 🐳 Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t project-name .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 project-name
   ```

### 📈 Visualizations
Visualizations are pre-generated and stored in the `Visualization_images` directory. These include:
- 📊 Score distributions
- 🔥 Correlation heatmaps
- 📦 Boxplots of scores by category

## 🛠️ Development
### 📂 Code Structure
- **`src`**: Contains the core logic of the application, including error handling (`exception.py`), logging (`logger.py`), and utility functions.
- **Pipelines**: Training and prediction workflows are implemented in `predict_pipeline.py`.

### 🧪 Testing
Unit tests can be added in the `tests` directory (not present but recommended).

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Feel free to explore the code and provide feedback! 😊
