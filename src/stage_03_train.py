from src.utils.all_utils import read_yaml,create_directory,save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib

def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    artifacts_dir  = config["artifacts"]["artifacts_dir"]

    split_data_dir  = config["artifacts"]["split_data_dir"]
    split_data_dir_path = os.path.join(artifacts_dir,split_data_dir)

    train_data_file = config["artifacts"]["train"]
    train_data_path = os.path.join(split_data_dir_path,train_data_file)

    train = pd.read_csv(train_data_path)

    train_y = train["quality"]
    train_x = train.drop("quality",axis=1)

    alpha = params["model_params"]["ElasticNet"]["alpha"]
    l1_ratio = params["model_params"]["ElasticNet"]["l1_ratio"]
    random_state = params["base"]["random_state"]

    El_Model = ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
    El_Model.fit(train_x,train_y)

    model_dir = config["artifacts"]["model_dir"]
    model_filename = config["artifacts"]["model_filename"]

    model_dir = os.path.join(artifacts_dir,model_dir)
    create_directory(dirs=[model_dir])
    model_path = os.path.join(model_dir,model_filename)

    joblib.dump(El_Model,model_path)

    print("Model Training is Done")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    parsed_args = args.parse_args()
    # print(parsed_args.config)
    train(config_path=parsed_args.config,params_path=parsed_args.params)