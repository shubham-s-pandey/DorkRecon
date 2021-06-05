#!/usr/bin/env python3
import sys , argparse , webbrowser

def logo():
	print ('\033[92m' + """
 ____________________________________________________________________________
|	 ____             _    ____                      		     |
|	|  _ \  ___  _ __| | _|  _ \ ___  ___ ___  _ __   		     |
|	| | | |/ _ \| '__| |/ / |_) / _ \/ __/ _ \| '_ \ 		     |
|	| |_| | (_) | |  |   <|  _ <  __/ (_| (_) | | | |		     |
|	|____/ \___/|_|  |_|\_\_| \_\___|\___\___/|_| |_|		     |
|									     |
|			 # Coded By SHUBHAM PANDEY - @shubham-s-pandey	     |
|____________________________________________________________________________|
   
 Credit: Shubham Pandey               Author: @shubham-s-pandey  
 Github: https://github.com/shubham-s-pandey/
                                                     
""" + '\033[00m')
logo()
print(('\033[91m' + "[!]Show options : python3 %s -d example.com -a       "%sys.argv[0]  + '\033[00m'))
print(('\033[91m' + "[!]Save as HTML File : python3 %s -d example.com -o  "%sys.argv[0]  + '\033[00m'))
print(('\033[91m' + "[!]Example Usage: python3 %s -d example.com -g 1     "%sys.argv[0]  + '\033[00m'))

if sys.version_info[0] < 2:
	print(('\033[91m' + "[!]" + '\033[00m')+" Python 3 required")
	exit()

parser = argparse.ArgumentParser()
parser.add_argument('-a',help='Show all options',required=False,action='store_true')
parser.add_argument('-o',help='Save as HTML output',required=False,action='store_true')
parser.add_argument('-d',help='Enter domain name {Example : example.com} ',required=True)
parser.add_argument('-g',help='Google Dorks ',required=False)
arg = parser.parse_args()


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()
args = parser.parse_args()
target = f'{args.d}'
if args.o == True:
	print('\033[96m' + f"""[+]Saved as {args.d}.html """ + '\033[00m')
	with open(f'{args.d}.html', 'w') as myFile:
	    myFile.write('<html>')
	    myFile.write('<body>')
	    myFile.write(' <table style="font-family: Verdana, sans-serif;font-size: 30px;margin-left: auto; margin-right: auto;" >')

	    myFile.write(' <h1 style=" border:5px solid black;  background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red);"><center>DorkRecon</center></h2>')
	    myFile.write(' <style>    th    {      background-image: linear-gradient(blue, cyan);      height:30px;    }    table,th,td    {      border:5px solid black;    }    table    {      width:100%;      color:black;        }  </style>')

	    myFile.write('<tr>    <th>Recon</th>    <th>Link</th>  </tr>')
	    myFile.write("""
	<tr><td>1 : Directory Listing</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" intitle:index of'> Dork </a>  </td></tr><tr><td>2 : Configuration file</td><td><a href='https://www.google.com/search?q=site:"""+target+""" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini'> Dork </a>   </td></tr><tr><td>3 : Database File</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" ext:sql | ext:dbf | ext:mdb'> Dork </a>  </td></tr><tr><td>4 : Wordpress file</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download'> Dork </a>  </td></tr><tr><td>5 : Log File</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" ext:log'> Dork </a>   </td></tr><tr><td>6 : Backup and old files</td><td><a href='https://www.google.com/search?q=site:"""+target+""" ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'> Dork </a>   </td></tr><tr><td>7 : Login Pages</td><td>  <a href='https://www.google.com/search?q=site:"""+target+""" inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth'> Dork </a> </td></tr><tr><td>8 : Apache Config files</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" filetype:config apache'> Dork </a>  </td></tr><tr><td>9 : Robots.txt file</td><td> <a href='https://www.google.com/search?q="""+target+"""/robots.txt'> Dork </a>  </td></tr><tr><td>10 : DomainEye</td><td> <a href='https://domaineye.com/similar/"""+target+"""'> Dork </a>  </td></tr><tr><td>11 : Publicly Exposed Documents</td><td><a href='https://www.google.com/search?q=site:"""+target+""" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'> Dork </a>   </td></tr><tr><td>12 : Finding Backdoors</td><td> <a href='https://www.google.com/search?q=site:"""+target+"""  inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor'> Dork </a>  </td></tr><tr><td>13 : Install ssetup files</td><td> <a href='https://www.google.com/search?q=site:"""+target+"""  inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config'> Dork </a>  </td></tr><tr><td>14 : Open Redirects</td><td><a href='https://www.google.com/search?q=site:"""+target+""" inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http'> Dork </a>   </td></tr><tr><td>15 : Apache Struts RCE</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" ext:action | ext:struts | ext:do'> Dork </a>  </td></tr><tr><td>16 : 3rd party exposure</td><td> <a href='http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com | site:*.atlassian.net | site:bitbucket.org """+target+"""'> Dork </a>  </td></tr><tr><td>17 : Check security headers</td><td> <a href='https://securityheaders.com/?q="""+target+"""&followRedirects=on'> Dork </a>  </td></tr><tr><td>18 : Gitlab</td><td> <a href='https://www.google.com/search?q=inurl:gitlab """+target+"""'> Dork </a>  </td></tr><tr><td>19 : Find pastebin entries</td><td><a href='https://www.google.com/search?q=site:pastebin.com """+target+"""'> Dork </a>   </td></tr><tr><td>20 : Employees on linkedin</td><td><a href='https://www.google.com/search?q=site:linkedin.com employees """+target+"""'> Dork </a>   </td></tr><tr><td>21 : .htacess sensitive files</td><td><a href='https://www.google.com/search?q=site:"""+target+""" inurl:/phpinfo.php | inurl:.htaccess'> Dork </a>   </td></tr><tr><td>22 : Find Subdomains</td><td> <a href='https://www.google.com/search?q=site:*."""+target+"""'> Dork </a>  </td></tr><tr><td>23 : Find sub-subdomains</td><td><a href='https://www.google.com/search?q=site:*.*."""+target+"""'> Dork </a>   </td></tr><tr><td>24 : Find Wordpress #2</td><td> <a href='https://www.google.com/search?q=site:"""+target+""" inurl:wp-content | inurl:wp-includes'> Dork </a>  </td></tr><tr><td>25 : Search in bitbucket and atlassian</td><td><a href='https://www.google.com/search?q=site:atlassian.net | site:bitbucket.org """+target+"""'> Dork </a>   </td></tr><tr><td>26 : Passive tools</td><td>  <a href='https://community.riskiq.com/search/"""+target+"""'> Dork </a> </td></tr><tr><td>27 : Search in stackoverflow</td><td><a href='https://www.google.com/search?q=site:stackoverflow.com """+target+"""'> Dork </a>   </td></tr><tr><td>28 : Find Wordpress [wayback machine]</td><td> <a href='http://wwwb-dedup.us.archive.org:8083/cdx/search?url="""+target+"""/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='> Dork </a>  </td></tr><tr><td>29 : Search in github</td><td> <a href='https://github.com/search?q=*."""+target+"""'> Dork </a>  </td></tr><tr><td>30 : Search in openbugbounty</td><td><a href='https://www.openbugbounty.org/search/?search="""+target+"""'> Dork </a>   </td></tr><tr><td>31 : Search in reddit</td><td><a href='https://www.reddit.com/search/?q="""+target+"""'> Dork </a>   </td></tr><tr><td>32 : Test Crossdomain</td><td> <a href='https://www.google.com/search?q="""+target+"""/crossdomain.xml'> Dork </a>  </td></tr><tr><td>33 : Check in threatcrowd</td><td><a href='https://threatcrowd.org/domain.php?domain="""+target+"""'> Dork </a>   </td></tr><tr><td>34 : Youtube</td><td> <a href='https://www.youtube.com/results?search_query="""+target+"""'> Dork </a>  </td></tr><tr><td>35 : DigitalOcean Spaces</td><td> <a href='https://www.google.com/search?q=site:digitaloceanspaces.com """+target+"""'> Dork </a>  </td></tr><tr><td>36 : find .swf file</td><td> <a href='https://www.google.com/search?q=inurl:"""+target+""" ext:swf'> Dork </a> </td></tr><tr><td>37 : find .swf yandex</td><td><a href='https://yandex.com/search/?text=site:"""+target+""" mime:swf'> Dork </a>   </td></tr><tr><td>38 : find .swf in wayback</td><td><a href='https://web.archive.org/cdx/search?url="""+target+"""/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000'> Dork </a>   </td></tr><tr><td>39 : Search in wayback machine #2</td><td><a href='https://web.archive.org/cdx/search?url="""+target+"""/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000'> Dork </a>   </td></tr><tr><td>40 : Search in wayback #3</td><td> <a href='https://web.archive.org/web/*/"""+target+"""/*'> Dork </a>  </td></tr><tr><td>41 : Reverse IP look</td><td> <a href='https://viewdns.info/reverseip/?host="""+target+"""&t=1'> Dork </a>  </td></tr><tr><td>42 : traefik</td><td><a href='https://www.google.com/search?q=intitle:traefik inurl:8080/dashboard"""+target+"""'> Dork </a>   </td></tr><tr><td>43 : Cloudstorage and buckets</td><td> <a href='https://cse.google.com/cse?cx=002972716746423218710:veac6ui3rio#gsc.tab=0&gsc.q="""+target+"""'> Dork </a>  </td></tr><tr><td>44 : s3 buckets</td><td> <a href='https://www.google.com/search?q=site:.s3.amazonaws.com """+target+"""'> Dork </a>  </td></tr><tr><td>45 : Source code public www</td><td><a href='https://publicwww.com/websites/%22"""+target+"""%22/'> Dork </a>   </td></tr><tr><td>46 : Check in censys[IP4]</td><td>  <a href='https://censys.io/ipv4?q="""+target+"""%22/'> Dork </a> </td></tr><tr><td>47 : Check in censys[Domains]</td><td><a href='https://censys.io/domain?q="""+target+"""'> Dork </a>   </td></tr><tr><td>48 : Check in censys certs</td><td><a href='https://censys.io/certificates?q="""+target+"""%22/'> Dork </a>   </td></tr><tr><td>49 : Search in shodan</td><td><a href='https://www.shodan.io/search?query="""+target+"""'> Dork </a>   </td></tr><tr><td>50 : CVE 2020-0646 Sharepoint rce</td><td> <a href='https://www.google.com/search?q=.sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec site:"""+target+"""'> Dork </a>  </td></tr><tr><td>51 : API Endpoints wsdl</td><td>  <a href='https://www.google.com/search?q=site:"""+target+""" filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl'> Dork </a> </td></tr><tr><td>52 : Github gist searches</td><td> <a href='https://gist.github.com/search?q=*."""+target+"""'> Dork </a>  </td></tr><tr><td>53 : Search in ct logs</td><td> <a href='https://crt.sh/?q="""+target+"""'> Dork </a>  </td></tr><tr><td>54 : Plaintext password leak</td><td><a href='https://www.google.com/search?q=site:throwbin.io """+target+"""'> Dork </a>   </td></tr><tr><td>55 : Whatcms</td><td> <a href='https://whatcms.org/?s="""+target+"""'> Dork </a> </td></tr><tr><td>56 : JIRA Desk</td><td> <a href='https://www.google.com/search?q=inurl: """+target+"""intitle:JIRA login'> Dork </a> </td></tr>
	""")    



	    myFile.write('</tr>')
	    myFile.write('</table>')
	    myFile.write(' <h2><center>Created by Shubham Pandey</center></h2>')
	    myFile.write('</body>')
	    myFile.write('</html>')

if args.a == True:
	print ('\033[96m' + """

Techniques:

 -1 : Directory Listing
 -2 : Configuration file
 -3 : Database File
 -4 : Wordpress file
 -5 : Log File
 -6 : Backup and old files
 -7 : Login Pages
 -8 : Apache Config files
 -9 : Robots.txt file
 -10 : DomainEye
 -11 : Publicly Exposed Documents
 -12 : Finding Backdoors
 -13 : Install ssetup files
 -14 : Open Redirects
 -15 : Apache Struts RCE
 -16 : 3rd party exposure
 -17 : Check security headers
 -18 : Gitlab
 -19 : Find pastebin entries
 -20 : Employees on linkedin
 -21 : .htacess sensitive files
 -22 : Find Subdomains
 -23 : Find sub-subdomains
 -24 : Find Wordpress #2
 -25 : Search in bitbucket and atlassian
 -26 : Passive tools
 -27 : Search in stackoverflow
 -28 : Find Wordpress [wayback machine]
 -29 : Search in github
 -30 : Search in openbugbounty
 -31 : Search in reddit
 -32 : Test Crossdomain
 -33 : Check in threatcrowd
 -34 : Youtube
 -35 : DigitalOcean Spaces
 -36 : find .swf file
 -37 : find .swf yandex
 -38 : find .swf in wayback
 -39 : Search in wayback machine #2
 -40 : Search in wayback #3
 -41 : Reverse IP look
 -42 : traefik
 -43 : Cloudstorage and buckets
 -44 : s3 buckets
 -45 : Source code public www
 -46 : Check in censys[IP4]
 -47 : Check in censys[Domains]
 -48 : Check in censys certs
 -49 : Search in shodan
 -50 : CVE 2020-0646 Sharepoint rce
 -51 : API Endpoints wsdl
 -52 : Github gist searches
 -53 : Search in ct logs
 -54 : Plaintext password leak
 -55 : Whatcms
 -56 : JIRA Desk



""" + '\033[00m')


if args.g == "1":
	url = f'site:{args.d} intitle:index of'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "2":
	url = f'site:{args.d} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "3":
	url = f'site:{args.d} ext:sql | ext:dbf | ext:mdb'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "4":
	url = f'site:{args.d} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "5":
	url = f'site:{args.d} ext:log'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "6":
	url = f'site:{args.d} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "7":
	url = f'site:{args.d} inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "8":
	url = f'site:{args.d} filetype:config apache'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "9":
	url = f'{args.d}/robots.txt'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "10":
	url = f'https://domaineye.com/similar/{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "11":
	url = f'site:{args.d} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "12":
	url = f'site:{args.d}  inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "13":
	url = f'site:{args.d}  inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "14":
	url = f'site:{args.d} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "15":
	url = f'site:{args.d} ext:action | ext:struts | ext:do'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "16":
	url = f'site:http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com | site:*.atlassian.net | site:bitbucket.org {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "17":
	url = f'https://securityheaders.com/?q={args.d}&followRedirects=on'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "18":
	url = f'inurl:gitlab {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "19":
	url = f'site:pastebin.com {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "20":
	url = f'site:linkedin.com employees {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "21":
	url = f'site:{args.d} inurl:/phpinfo.php | inurl:.htaccess'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "22":
	url = f'site:*.{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "23":
	url = f'site:*.*.{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "24":
	url = f'site:{args.d} inurl:wp-content | inurl:wp-includes'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "25":
	url = f'site:atlassian.net | site:bitbucket.org {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "26":
	url = f'https://community.riskiq.com/search/{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "27":
	url = f'site:stackoverflow.com {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "28":
	url = f'http://wwwb-dedup.us.archive.org:8083/cdx/search?url={args.d}/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "29":
	url = f'https://github.com/search?q=*.{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "30":
	url = f'https://www.openbugbounty.org/search/?search={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "31":
	url = f'https://www.reddit.com/search/?q={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "32":
	url = f'{args.d}/crossdomain.xml'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "33":
	url = f'https://threatcrowd.org/domain.php?domain={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "34":
	url = f'https://www.youtube.com/results?search_query={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "35":
	url = f'site:digitaloceanspaces.com {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "36":
	url = f'inurl:{args.d} ext:swf'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "37":
	url = f'https://yandex.com/search/?text=site:{args.d} mime:swf'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "38":
	url = f'https://web.archive.org/cdx/search?url={args.d}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "39":
	url = f'https://web.archive.org/cdx/search?url={args.d}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "40":
	url = f'https://web.archive.org/web/*/{args.d}/*'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "41":
	url = f'https://viewdns.info/reverseip/?host={args.d}&t=1'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "42":
	url = f'intitle:traefik inurl:8080/dashboard {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "43":
	url = f'https://cse.google.com/cse?cx=002972716746423218710:veac6ui3rio#gsc.tab=0&gsc.q={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "44":
	url = f'site:.s3.amazonaws.com {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "45":
	url = f'https://publicwww.com/websites/%22{args.d}%22/'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "46":
	url = f'https://censys.io/ipv4?q={args.d}%22/'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "47":
	url = f'https://censys.io/domain?q={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "48":
	url = f'https://censys.io/certificates?q={args.d}%22/'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "49":
	url = f'https://www.shodan.io/search?query={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "50":
	url = f'site:{args.d} .sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "51":
	url = f'site:{args.d} filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "52":
	url = f'https://gist.github.com/search?q=*.{args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "53":
	url = f'https://crt.sh/?q={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "54":
	url = f'site:throwbin.io {args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "55":
	url = f'https://whatcms.org/?s={args.d}'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
if args.g == "56":
	sample_uri = f'{args.d}'
	url = f'inurl:{args.d} intitle:JIRA login'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)
	url = sample_uri.split(".")[0]+'.atlassian.net/servicedesk/customer/user/signup'
	webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("firefox"))
	webbrowser.get('firefox').open(url)


