import mysql.connector

try:

	connection = mysql.connector.connect(host='localhost',
										database='wireless_check',
										user='root',
										password='')
	cursor = connection.cursor()
	mysql_insert_query="""INSERT INTO result_radio (loader,mac_addr_wap,ssid,channel,signal_str) VALUES(%s,%s,%s,%s,%s)"""
	record = ("loader","wap","ssid","1","sig_str")
	cursor.execute(mysql_insert_query, record)
	connection.commit()
	print('sukses input')
except mysql.connector.Error as error:
	print('failed insert'.format(error))
