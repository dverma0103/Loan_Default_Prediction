{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9f9e6573-fa1d-46ba-b64e-60d55af5e751",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PreProcesing Complete.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder, StandardScaler\n",
    "import joblib\n",
    "import os\n",
    "\n",
    "def preprocess_data(input_path, output_path):\n",
    "    data = pd.read_csv(input_path)\n",
    "    data.columns = data.columns.str.strip()\n",
    "    le = LabelEncoder()\n",
    "    data['education'] = le.fit_transform(data['education'])\n",
    "    data['self_employed'] = le.fit_transform(data['self_employed'])\n",
    "    data['loan_status'] = le.fit_transform(data['loan_status'])\n",
    "    x = data.drop(['loan_id', 'loan_status'], axis=1)\n",
    "    y = data[\"loan_status\"]\n",
    "    scaler = StandardScaler()\n",
    "    x_scaled = scaler.fit_transform(x)\n",
    "    processed_data = pd.DataFrame(x_scaled, columns=x.columns)\n",
    "    processed_data['loan_status'] = y\n",
    "    os.makedirs(os.path.dirname(output_path), exist_ok = True)\n",
    "    processed_data.to_csv(output_path, index=False)\n",
    "    joblib.dump(scaler, r'C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\models\\preprocessing_pipeline.pkl')\n",
    "    print(\"PreProcesing Complete.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    preprocess_data(\n",
    "        input_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\data\\raw\\loan_approval_dataset.csv\",\n",
    "        output_path = r\"C:\\Users\\Deepak Verma\\OneDrive\\Documents\\Loan_Default_Prediction\\data\\processed\\loan_data_processed.csv\"\n",
    "    )\n"
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
