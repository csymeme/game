#_*_ coding: utf-8_*_
import json
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def load():
	data=[]
	for line in open(r'C:\Users\csy\Desktop\data1.json', 'r'):
		data.append(json.loads(line))
	return data

def loop_data(o,k=""):
	global json_ob,c_line
	if isinstance(o,dict):
		for key,value in o.items():
			if(k==''):
				loop_data(value,key)
			else:
				loop_data(value,k+'.'+key)
	elif isinstance(o,list):
		if not k in json_ob:
			json_ob[k]={}
		content = ";".join(o)
		json_ob[k][c_line]=content

	else:
		if not k in json_ob:
			json_ob[k]={}
		json_ob[k][c_line]=o

def get_title_rows(json_ob):
	title=[]
	row_num=0
	rows=[]
	for key in json_ob:
		title.append(key)
		v=json_ob[key]
		if len(v)>row_num:
			row_num=len(v)
		continue
	for i in range(row_num):
		row={}
		for k in json_ob:
			v=json_ob[k]
			if i in v.keys():
				row[k]=v[i]
			else:
				row[k]=''
		rows.append(row)
	return title,rows

def write_csv(title, rows, csv_file_name):
    with open(csv_file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=title)
        writer.writeheader()
        writer.writerows(rows)

def json_to_csv(object_list):
    global json_ob, c_line
    json_ob = {}
    c_line = 0
    for ov in object_list :
        loop_data(ov)
        c_line += 1
    title, rows = get_title_rows(json_ob)
    write_csv(title, rows, r'C:\Users\csy\Desktop\test.csv')

json_to_csv(load())