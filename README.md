## Site mirror Telegram upload

Wget mirror a site to a telegram channel

I'm using google cloud shell to avoid the double bandwidth myself

Max limit of storage is 45 GB in /root for google cloud shell

## TODO

- [ ] Init db
- [ ] Crawl site like wget no-parent
    - [ ] Save all the urls to the db file
- [ ] Start downloading all via the links from the db
- [ ] Whenever a download is done successfully write to db
- [ ] Start upload to telegram immediately
- [ ] Whenever upload is done successfully write tg:FileID to db
    - [ ] And delete local file
