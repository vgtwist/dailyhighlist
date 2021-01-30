import urllib.request
import json
from urllib.request import Request, urlopen

### -- Library of common modules  -----------------

def getheaderfromfile (filename):
	file = open(filename, "r")
	header = file.readline()
	header = header.replace ("\n", "")
	file.close()
	return header

def getcreattableddl (tablename, header, delim):
	collist = header.split(delim)
	returnval = "CREATE TABLE "+tablename+" \n"
	colprint = "("
	for row in range (len(collist)):
		if row != len(collist) -1:
			colprint += collist[row] + " varchar2(100),\n"
		else:
			colprint += collist[row] + " varchar2(100)\n"

	colprint += ");"
	return (returnval + colprint)

def writestringtofile (filename, filebody):
	#------------------------------------------
	# Creates a file with filename and the contents with filebody
	#------------------------------------------

	file = open(filename, "w")
	file.write (filebody)
	file.close()

def getsqlldrctlhdr (tablename, header, delim):
	collist = header.split(delim)
	returnval = """options (skip=1)
          LOAD DATA
          INFILE '~.txt'
          BADFILE '~.bad'
          APPEND INTO TABLE ~
          FIELDS TERMINATED BY '#'
          TRAILING NULLCOLS
		  """

	returnval = returnval.replace ("~", tablename)
	returnval = returnval.replace ("#", delim)

	colprint = "("
	for row in range (len(collist)):
		if row != len(collist) -1:
			colprint += collist[row] + " ,\n"
		else:
			colprint += collist[row] + " \n"

	colprint += ")"
	return (returnval + colprint)

def urlget (url):
	#--------------------------------------------------------
	# Accepts a url and returns a string with the url contents
	#--------------------------------------------------------

	retval = ""
	try:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		retval = urlopen(req).read()
		return str(retval)

	except Exception as e:
		print (str(e))


def urlget_old (url):
	retval = ""
	try:
		html = urllib.request.urlopen (url)
		retval = html.read()
		return str(retval)

	except Exception as e:
		print (str(e))


def urlgetjsondict (url):
	req = urllib.request.Request(url)
	response = urllib.request.urlopen(req)
	data = response.read()
	data = data.decode("utf-8")
	data = data.replace ("(","")
	data = data.replace (")","")
	data = data.replace (";","")
	return json.loads(data)


def extractstring (find_in_string, start_find_sting, extract_length=0, end_find_sting=">>>>"):
    #-------------------------------------------------------------
    #  find_in_string -- string to find in
    #  start_find_sting -- start string sequence
    #  extract_length -- number of chars to extract
    #  end_find_sting -- end string sequence
    #-------------------------------------------------------------

    startplace = find_in_string.find (start_find_sting) + len(start_find_sting)
    if extract_length == 0:
        snippet =  find_in_string [startplace:]
        returnstring = snippet
    else:
        snippet =  find_in_string [startplace:startplace + extract_length]
        endplace = snippet.find(end_find_sting)
        returnstring = snippet[:endplace]

    return returnstring
