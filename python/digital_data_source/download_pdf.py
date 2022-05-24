import urllib.request
import announcement_list

def getFile(url, file_name):
    u = urllib.request.urlopen(url)
    f = open("./announcement/"+file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()

if __name__ == '__main__':
    date = announcement_list.select_all()
    for value in date:
        file_name = value['ts_code'][:6]+"_"+value['title']+".pdf"
        try:
            getFile(value['src_url'],file_name)
        except:
            print(value['id'])