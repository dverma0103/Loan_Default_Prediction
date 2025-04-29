{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8b5ed03b-713a-45b6-b520-326b0ea1a4d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\models\\rf_model.pkl\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00      2656\n",
      "           1       1.00      0.99      1.00      1613\n",
      "\n",
      "    accuracy                           1.00      4269\n",
      "   macro avg       1.00      1.00      1.00      4269\n",
      "weighted avg       1.00      1.00      1.00      4269\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.metrics import classification_report\n",
    "import joblib\n",
    "\n",
    "def evaluate(model_path, data_path):\n",
    "    data = pd.read_csv(data_path)\n",
    "    x = data.drop(\"loan_status\", axis = 1)\n",
    "    y = data[\"loan_status\"]\n",
    "    model = joblib.load(model_path)\n",
    "    preds = model.predict(x)\n",
    "    print(f\"Model: {model_path}\")\n",
    "    print(classification_report(y, preds))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    evaluate(\n",
    "        model_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\models\\rf_model.pkl\",\n",
    "        data_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\data\\processed\\loan_data_processed.csv\"\n",
    "    )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
