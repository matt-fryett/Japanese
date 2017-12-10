import sqlite3
from random import randint
from random import choice

conn = sqlite3.connect('japanese.db')
# c = conn.cursor()
# c.execute("SELECT * FROM sqlite_sequence")
# rows = c.fetchall()
# for r in rows:
#     try:
#         print(r[0])
#         c.execute("UPDATE "+r[0]+" SET jfbp_lv=1 WHERE jfbp_lv=0")
#     except Exception as e:
#         print(str(e))
# conn.commit()
# conn.close()
# exit()


def get(typ):
    c.execute("SELECT * FROM "+typ+" ORDER BY encountered-correct ASC,RANDOM()")
    row = c.fetchone()
    if not row:
        return "","",""
    else:
        return row[0], row[1], row[2]

for i in range(100):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_sequence ORDER BY RANDOM()")
    tab = c.fetchone()[0]
    sid,sjp,sen = get(tab)

    foundSub = False
    subs = {}
    sub = ""
    for s in sjp:
        if foundSub and s=="]":
            sub_id,sub_type = tuple(sub.split(":"))
            sub_types = sub_type.split("|")
            subs[sub] = get(choice(sub_types))
            foundSub = False
        elif foundSub:
            sub+=s
        elif not foundSub and s=="[":
            foundSub = True
            sub = ""
    while "[" in sjp or "]" in sjp:
        #print(sjp,subs)
        for k in subs:
            sjp = sjp.replace("["+k+"]",subs[k][1][0])

    while "[" in sen or "]" in sen:
        for k in subs:
            sen = sen.replace("["+k+"]",subs[k][1][1])

    print(sjp)
    print(sen)
    print("------------------")