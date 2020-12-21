import sys
import requests
import json
import os

S3_URL = "https://nyc-tlc.s3.amazonaws.com"
# S3_ALT_URL = "https://s3.amazonaws.com/nyc-tlc"  (for fhv, hvfhv files)

datatypes = ["yellow", "green", "fhv", "hvfhv"]

# Example URLs:
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2019-06.csv
# https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2019-06.csv


def download_file(url):
    filename = url.split("/")[-1] 
    print ("Downloading: " + filename)
    with open('output/' + filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
        # TODO: continue if you can't find the resource

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

    for file in os.listdir('output'):
        n = file.find("_tripdata_") + len("_tripdata") + 1
        year = file[n:n+4]

        if year not in output_list.keys():
            output_list[year] = [file]
        else:
            output_list[year].append(file)
    return output_list



def main(argv):
    assemble()
    sys.exit(1)

    for year in range(2009, 2021):
        for month in range(1, 13):
            for datatype in datatypes:
                filename = datatype + "_tripdata_" + str(year) + "-" + str(month).zfill(2) + ".csv"

                url = S3_URL + "/trip+data/" + filename
                # print (url)
                if not os.path.exists('output/' + filename):
                    download_file(url)
                else:
                    print(filename + " already exists - skipping...")
        # break # pause after one year




if __name__ == "__main__":
    main(sys.argv[1:])




