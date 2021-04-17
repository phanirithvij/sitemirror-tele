# https://stackoverflow.com/a/6747761/8608146

wget --spider --recursive --no-verbose -U "eye02" -R "index.html*" -m -np \
 --output-file=wgetlog.txt "https://the-eye.eu/public/Comics/DC%20Chronology/"

sed -n "s@.\+ URL:\([^ ]\+\) .\+@\1@p" wgetlog.txt | sed "s@&@\&amp;@" > sedlog.txt
