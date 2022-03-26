import os
from dotenv import load_dotenv
import pandas as pd

def get_bitwarden_csv_contents(env_file):
    load_dotenv(env_file)
    bitwarden_csv_file = str(os.getenv("BITWARDEN_CSV_FILE"))
    bw_csv_content = pd.read_csv(bitwarden_csv_file)
    return bw_csv_content


def fetch_bitwarden_data_into_dic(bw_df):
    d = {
        "url" : [],
        "username" : [],
        "password" : [],
        "name" : []
    }
    
    bw_df.drop(bw_df[bw_df["type"] == "note"].index, inplace=True)

    urls = bw_df["login_uri"]
    usernames = bw_df["login_username"]
    passwords = bw_df["login_password"]
    names = bw_df["name"]
    
    for url in list(urls):
        d["url"].append(url)
    for username in list(usernames):
        d["username"].append(username)
    for password in passwords:
        d["password"].append(password)
    for name in names:
        d["name"].append(name)
    
    return d

def create_last_pass_csv(d):
    try:
        last_pass_csv = pd.DataFrame(d)
        last_pass_csv.to_csv("last_pass.csv", index=False)
        print("Lastpass csv file generated")
    except:
        print("Lastpass csv file creation error")


if "__main__" == __name__:
    env_file = "filepath.env"
    bw_csv_content = get_bitwarden_csv_contents(env_file)
    dic_content = fetch_bitwarden_data_into_dic(bw_csv_content)
    create_last_pass_csv(dic_content)