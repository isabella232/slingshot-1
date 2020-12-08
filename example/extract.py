import sys
import requests
import json

S3_URL = "https://nyc-tlc.s3.amazonaws.com"
LOTUS_NODE = "http://34.216.9.61:28001/rpc/v0"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBbGxvdyI6WyJyZWFkIiwid3JpdGUiLCJzaWduIiwiYWRtaW4iXX0.B4qGPtfsF7KwK1kg0nakQbaJC3-SyxqYPKvW1hU7GKU"
# S3_ALT_URL = "https://s3.amazonaws.com/nyc-tlc"

datatypes = ["yellow", "green", "fhv", "hvfhv"]

# Example:  https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-06.csv
#             https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2019-06.csv


def lotus_cmd(method,data={}, files=[], debug=False):
    # Do a chain API call
    headers = {"Authorization": "Bearer " + TOKEN}
    data["jsonrpc"] = "2.0"
    data["method"] = "Filecoin." + method
    data["id"] = 2
    data["params"] = []
    r = requests.post(LOTUS_NODE, data=json.dumps(data), headers=headers)
    # print(r.status_code)
    # print(r.reason)
    j = json.loads(r.text)
    return j['result']

def download_file(url):
    filename = url.split("/")[-1] 
    print ("Downloading: " + filename)
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            #TODO: Upgrade progress bar with percentage or time estiamte
            print(total_length)
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
    f.close()

# Can't import files into the Lotus library remotely
def client_import(file):
    files={'files': open(filename,'rb')}
    values={'upload_file' : 'file.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files,data=values)

    print ("Importing file to Lotus")


def main(argv):

    response = lotus_cmd("ChainHead")
    print(response)
    sys.exit(0)
    # year = "2019"
    # datatype = "yellow"
    # month = "06"


    for year in range(2009, 2021): 
        for month in range(1, 13):
            for datatype in datatypes:
                filename = datatype + "_tripdata_" + str(year) + "-" + str(month).zfill(2) + ".csv"

                url = S3_URL + "/trip+data/" + filename
                # print (url)
                download_file(url)
                cid = client_import(filename)
                # make deal
                break    # Temporary to test for one month


if __name__ == "__main__":
    main(sys.argv[1:])




