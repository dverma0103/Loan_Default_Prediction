{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "67919d95-1917-4421-9e2d-7c6672cd54e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Trained and Saved\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from xgboost import XGBClassifier\n",
    "import joblib\n",
    "import os\n",
    "\n",
    "def train_models(data_path, rf_path, xgb_path):\n",
    "    data = pd.read_csv(data_path)\n",
    "    x = data.drop(\"loan_status\", axis = 1)\n",
    "    y = data[\"loan_status\"]\n",
    "    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)\n",
    "    rf = RandomForestClassifier()\n",
    "    rf.fit(x_train, y_train)\n",
    "    joblib.dump(rf, rf_path)\n",
    "    xgb = XGBClassifier()\n",
    "    xgb.fit(x_train, y_train)\n",
    "    joblib.dump(xgb, xgb_path)\n",
    "    print(\"Model Trained and Saved\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    train_models(\n",
    "        data_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\data\\processed\\loan_data_processed.csv\",\n",
    "        rf_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\models\\rf_model.pkl\",\n",
    "        xgb_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\models\\xgb_model.pkl\"\n",
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
