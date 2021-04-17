filename = "wgetlog.txt"
with open(filename, 'r') as f:
    with open("urls.txt", 'w+') as u:
        urls = []
        for line in f.readlines():
            if "URL:" in line.strip():
                urls.append(line.strip())
        for url in urls:
            print(url.split("URL:")[1].strip().split(" ")[0], file=u)
