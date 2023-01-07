from src.utils.all_utils import read_yaml,create_directory,save_local_df,save_reports
import argparse
import pandas as pd
import os
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import joblib
import numpy as np


def evaluation_metrics(actual_values,predicted_values):
    rmse = np.sqrt(mean_squared_error(actual_values,predicted_values))
    mae = mean_absolute_error(actual_values,predicted_values)
    r2_score_ = r2_score(actual_values,predicted_values)
    return rmse,mae,r2_score_

def evaluate(config_path):
    config = read_yaml(config_path)
    artifacts_dir  = config["artifacts"]["artifacts_dir"]

    split_data_dir  = config["artifacts"]["split_data_dir"]
    split_data_dir_path = os.path.join(artifacts_dir,split_data_dir)

    test_data_file = config["artifacts"]["test"]
    test_data_path = os.path.join(split_data_dir_path,test_data_file)

    test = pd.read_csv(test_data_path)

    test_y = test["quality"]
    test_x = test.drop("quality",axis=1)
    model_dir = config["artifacts"]["model_dir"]
    model_filename = config["artifacts"]["model_filename"]
    model_path = os.path.join(artifacts_dir,model_dir,model_filename)

    El_model=joblib.load(model_path)
    predicted_values = El_model.predict(test_x)

    rmse,mae,r2_score_ = evaluation_metrics(test_y,predicted_values)

    reports_dir = config["artifacts"]["reports_dir"]
    reports_dir_path = os.path.join(artifacts_dir,reports_dir)
    create_directory([reports_dir_path])
    reports_filename = config["artifacts"]["scores"]
    report_path = os.path.join(reports_dir_path,reports_filename)
    save_reports({"rmse_score":rmse,"mae_score":mae,"r2_score":r2_score_},reports_path=report_path)

    print("Model evaluation is Done")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    # args.add_argument("--params","-p",default="params.yaml")
    parsed_args = args.parse_args()
    # print(parsed_args.config)
    evaluate(config_path=parsed_args.config)

