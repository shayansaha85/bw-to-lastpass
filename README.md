[url=https://ibb.co/3r5XQrw][img]https://i.ibb.co/3r5XQrw/conversion.png[/img][/url]
# Import bitwarden passwords in lastpass

If you are switching from bitwarden to lastpass, then in the import section of lastpass you will not get the bitwarden option (current date). And the exported csv file from bitwarden is not compatible with lastpass for importing through generic csv file. This code will help you to convert the bitwarden csv file into a lastpass csv file.


## How to use?

First you need Python to be installed in your machine. If not, download it from : https://www.python.org and configure **pip**
- Clone this repository
```bash
    git clone https://github.com/shayansaha85/bw-to-lastpass.git
```
- Open command prompt or powershell in the repository folder and hit the below command to install the libraries
```
    pip install -r requirements.txt
```
- Export the passwords in CSV format from Bitwarden
- Inside filepath.env paste the path of the CSV file. If the path contains "\\" (single backslash), please replace it with "\\\\" (double backslash)
- Run **main.py** file with the below command :
```
    python main.py
```
- One CSV file will be generated in the root directory **last_pass.csv** which can be imported in the lastpass
