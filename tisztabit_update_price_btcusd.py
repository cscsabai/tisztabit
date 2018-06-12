#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime, time, json, socket, http.client
import urllib.request, urllib.parse, urllib.error
import pymysql as mdb

import tisztabit_conf as tconf

mdb.install_as_MySQLdb();

dbcon = mdb.connect(tconf.host, tconf.user, tconf.pass, tconf.db)
dbcur = dbcon.cursor()

conn = http.client.HTTPConnection("coincap.io")
conn.request('GET',urllib.parse.quote('/page/BTC'))
response = conn.getresponse()

res = json.loads(response.read().decode())


dbcur.execute(('update wp_posts set post_title="%d" where ID=1863;' )%( int(res['price'])))

dbcon.commit();
if 'dbcon' in globals(): dbcon.close();
