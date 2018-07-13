import urllib, httplib, re, urllib2, time, sys
userAGE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', userAGE)]
sitelist = []
comp = []
 
def header():
	print("""
  ########    ####  ##        ##    ######      ##########  
  ##     ##    ##   ###       ##  ##           ##        ##
  ##     ##    ##   ####      ##  ##           ##        ##
  ########     ##   ##  ##    ##  ##   ######  ##        ##
  ##     ##    ##   ##    ##  ##  ##     ##    ##        ##
  ##     ##    ##   ##      ####  ##     ##    ##        ##
  ########    ####  ##        ##   #######      ##########   

   _______BINGO v1.0-site collector using bing dork_________
                         *********gretz to all member of ICH             
""") 

def loader():
	animation = "|/-\|"
	for i in range(69):
		time.sleep(0.1)
		sys.stdout.write( animation[i % len(animation)])
		sys.stdout.flush()
	print("\n")
	

def dorker(dork,pages):
    d = urllib.quote(dork)
    p = 1
    m = pages * 10
    while p <= m:
        try:
            search = "http://www.bing.com/search?q=" + d +"&first=" + str(p)
            req = opener.open(search)
            source = req.read()
            sites = re.findall('<h2><a href="http://(.*?)"', source)
            sitelist.extend(sites)
            p += 10
        except urllib2.URLError:
            print ("url error")
            continue
        except urllib2.HTTPError:
            print ("http error")
            continue
        except IOError:
            continue
        except httplib.HTTPException:
            continue
    uniqsites = list(set(sitelist))  
    for line in uniqsites:
        sep = '/'
        build = "http://" + line.split(sep,1)[0]
        comp.append(build)
        print "\t\t" + build
    final1 = list(set(comp))
    l = "results" + str(len(final1)) + ".txt"
    foo = open(l,"w")
    for ss in final1:
        foo.write(ss + "\n")
    foo.close()
    
    print "\033[1;31m[OK] saved as " + l
    
    
header()
loader()
dr = raw_input('\033[1;31m Type Your dork\033[1;37m  :: ')
numpages = int(raw_input('\033[1;34m Number of pages to look for \033[1;37m :: '))
print ' \033[1;32m[>] Searching ...\033[1;37m  '
dorker(dr, numpages)
