.PHONY: requirements clean lint preprocess train predict pipeline

# ==========================================
# 1. ENVIRONMENT & MAINTENANCE
# ==========================================

# Install all project dependencies
requirements:
	pip install -r requirements.txt

# Remove compiled Python files and hidden caches to keep the repo clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .ipynb_checkpoints
	rm -rf .pytest_cache

# Format and lint the code to maintain Software Engineering standards
lint:
	black src/
	flake8 src/

# ==========================================
# 2. ML & KAGGLE LIFECYCLE PIPELINE
# ==========================================

# Step 1: Run feature engineering and save to data/processed/
preprocess:
	python src/preprocessing.py

# Step 2: Train the model and save the artifact to models/
train:
	python src/train.py

# Step 3: Run inference and save the submission.csv to outputs/
predict:
	python src/predict.py

# Execute the entire workflow end-to-end with one command
pipeline: preprocess train predict