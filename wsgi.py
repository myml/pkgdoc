
from os.path import isfile,isdir

def application(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/html')]
	start_response(status, response_headers)
	path=environ['PATH_INFO']
	if isfile(path):
		with open('static'+path,'r') as file:
			return [file.read()]
	if isdir(path):
		dir=os.listdir('static'+path)
		return ['<html><body>','\r\n'.join(['<a href="./%s" traget=_blank>%s</a><br/>'%(d,d) for d in dir]),'</body></html>']
	return ['not find']