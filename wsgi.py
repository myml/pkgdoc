
from os.path import isfile,isdir
import os

def application(environ, start_response):
	status = '200 OK'
	path=environ['PATH_INFO']
	if path=='/':
		path='/index.html'
	if path[-3:]=='css':
		response_headers = [('Content-type','text/css')]
	else:
		response_headers = [('Content-type','text/html')]
	start_response(status, response_headers)
	if isfile('static'+path):
		with open('static'+path,'r') as file:
			return [file.read()]
	if isdir('static'+path):
		dir=os.listdir('static'+path)
		return ['<html><body>','\r\n'.join(['<a href="%s/%s" traget=_blank>%s</a><br/>'%(path,d,d) for d in dir]),'</body></html>']
	return ['<h1>not find</h1>']