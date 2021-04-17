# https://stackoverflow.com/a/6747761/8608146
# https://unix.stackexchange.com/a/128476/312058

wget --spider --recursive --no-verbose -U "eye02" -R "index.html*" -m -np \
 "https://the-eye.eu/public/Comics/DC%20Chronology/" 2>&1 | tee -a wgetlog.txt

sed -n "s@.\+ URL:\([^ ]\+\) .\+@\1@p" wgetlog.txt | sed "s@&@\&amp;@" > sedlog.txt
