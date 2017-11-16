#/usr/bin/python2.7
#encoding=utf-8

import boto
import boto.s3.connection 
import sys

access = sys.argv[1]
secret = sys.argv[2]
print "access: %s; secret: %s " % (access, secret)
conn = boto.connect_s3(					\
		aws_access_key_id = access,		\
		aws_secret_access_key = secret, \
		host = "cephs3",					\
		is_secure=False,					\
		calling_format = boto.s3.connection.OrdinaryCallingFormat(),
		)
bucket=""
mybucket=""
def list_bucket():
	for bucket in conn.get_all_buckets():
		print "name: %s, create_time: %s" %(bucket.name, bucket.creation_date)

def list_all_content():
	for bucket in conn.get_all_buckets():
		for key in bucket.list():
			print "name: %s; size: %d; modified: %s" %(key.name, key.size, key.last_modified)

def list_content(bucket_name):
	for bucket in conn.get_all_buckets():
		if bucket.name == bucket_name:
			for key in bucket.list():
				print "name: %s; size: %d; modified: %s" % (key.name, key.size, key.last_modified)

def create_bucket(bucket_name):
	conn.create_bucket(bucket_name)

def delete_bucket(bucket_name):
	flag = False
	for bucket in conn.get_all_buckets():
		if bucket.name == bucket_name:
			conn.delete_bucket(bucket_name)
			flag = True
	if not flag:
		print "no such bucket"

def updatefile(bucket_name, key, file):
	if mybucket in conn.get_all_buckets():
		if mybucket.name == bucket_name:
			key = mybucket.new_key(key)
			key.set_contents_from_file(file)
	
def GetBucketAcl(bucket_name):
	bucket = conn.get_bucket(bucket_name)
	acl = bucket.get_acl()
	for grant in acl.acl.grants:
		print grant.permission, grant.display_name, grant.email_address, grant.id

def setBucketAcl(bucket_name):
	bucket = conn.get_bucket(bucket_name)
	bucket.set_acl("public-read")

def GetObject(bucket_name, key, dest_file):
	bucket = conn.get_bucket(bucket_name)
	k = bucket.lookup(key)
	k.get_contents_to_filename(dest_file)


if __name__ == "__main__":
	print "			\n  \
list_bucket: 		1\n	\
list_all_content: 	2\n	\
list_content: 		3\n	\
creat_bucket: 		4\n	\
delete_bucket: 		5\n	\
updatefile: 		6\n	\
GetbucketAcl: 		7\n	\
setbucketAcl: 		9\n	\
GetObject:		10\n\
exit:			100\n\
	"
	while True:
		no = int(raw_input("nu:  "))
		if no == 1:
			list_bucket()
		elif no == 2:
			list_all_content()
		elif no == 3:
			bucket_name = raw_input("select bucket:")
			list_content(bucket_name)
		elif no == 4:
			bucket_name = raw_input("input bucket_name: ")
			create_bucket(bucket_name)
		elif no == 5:
			bucket_name = raw_input("input bucket_name: ")
			delete_bucket(bucket_name)
		elif no == 6:
			bucket_name = raw_input("select bucket: ")
			key_name    = raw_input("set key: ")
			file 		= raw_input("file dir: ")
			updatefile(bucket_name, key_name, file)
		elif no == 7:
			bucket_name  = raw_input("select bucket: ")
			GetBucketAcl(bucket_name)
		elif no == 8:
			bucket_name = raw_input("select bucket: ")
			setBuckAcl(bucket_name)
		elif no == 9:
			bucket_name = raw_input("select bucket: ")
			key 		= raw_input("which file: ")
			file        = raw_input("save dir: ")
			GetObject(bucket_name, key, file )
		elif no == 100:
			sys.exit()
		else:
			print "input error,put again:"

