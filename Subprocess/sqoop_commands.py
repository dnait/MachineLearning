import commands
cmd = "sqoop eval --connect 'jdbc:mysql://quickstart.cloudera:3306/retail_db' --username retail_dba --password cloudera \
--query 'select * from departments'"

status, res = commands.getstatusoutput(cmd)
f = file("/home/cloudera/reporttext1.txt", 'w+')
f.writelines(res)
f.close()


