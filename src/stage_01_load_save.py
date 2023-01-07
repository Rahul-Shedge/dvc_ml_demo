from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd
import os



def get_data(config_path):
    config = read_yaml(config_path)
    # print(config)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path,sep=";")
    # print(df.head())

    # save dataset in local directory
    # create path to directiory artifacts/raw_local_dir/data.csv

    artifacts_dir  = config["artifacts"]["artifacts_dir"]
    raw_local_dir  = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_files"]

    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)
    # print(raw_local_file_path)
    create_directory(dirs=[raw_local_dir_path])
    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)
    df.to_csv(raw_local_file_path,sep=",",index=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_args = args.parse_args()

    print(parsed_args.config)

    get_data(config_path=parsed_args.config)