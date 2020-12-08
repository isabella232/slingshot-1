import sys
import requests
import json

S3_URL = "https://nyc-tlc.s3.amazonaws.com"
LOTUS_NODE = "http://34.216.9.61:28001/rpc/v0"
TOKEN = "REPLACE_ME"
# S3_ALT_URL = "https://s3.amazonaws.com/nyc-tlc"

datatypes = ["yellow", "green", "fhv", "hvfhv"]

# Example:  https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-06.csv
#             https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2019-06.csv


def lotus_cmd(method,data={}, files=[], debug=False):
    # Do a chain API call
    headers = {"Authorization": "Bearer " + TOKEN}
    data["jsonrpc"] = "2.0"
    data["method"] = "Filecoin." + method

    # This may need to be custom - make it part of the parameters passed in?
    data["id"] = 2
    data["params"] = []

    r = requests.post(LOTUS_NODE, data=json.dumps(data), headers=headers)
    # print(r.status_code)
    # print(r.reason)
    j = json.loads(r.text)
    return j['result']


# Can't import files into the Lotus library remotely
def client_import(file):
    files={'files': open(filename,'rb')}
    values={'upload_file' : 'file.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files,data=values)
    print ("Importing file to Lotus")
    return cid


def download_file(url):
    filename = url.split("/")[-1] 
    print ("Downloading: " + filename)
    with open('output/' + filename, 'wb') as f:
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


def assemble():
    output_list = {}

    for file in os.dirlist():
        if output_list[year] is None:
            output_list[year] = [filename]
        else:
            output_list[year].append(filename)

    json.dumps(output_list)



def main(argv):

    response = lotus_cmd("ChainHead")
    # print(response)

    # for testing
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

                # make deal
        break # pause after one year

    assemble()


if __name__ == "__main__":
    main(sys.argv[1:])




