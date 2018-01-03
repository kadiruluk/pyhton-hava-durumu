from sys import version_info
if version_info[0] == 2 and version_info[1] >= 2:
    from HTMLParser import HTMLParser
elif version_info[0] == 3:
    from html.parser import HTMLParser
else:
    from sys import exit
    print("Python yorumlayıcınız bu programı kullanamaz!")
    exit(1)
        html>  
         <head>
         <title>Başlık</title> 
         </head>

          <body>
          <span id="benimspan" class="7b"></span>
          </body>
          </html>

     from sys import version_info
if version_info[0] == 2 and version_info[1] >= 2:
    from HTMLParser import HTMLParser
elif version_info[0] == 3:
    from html.parser import HTMLParser
else:
    from sys import exit
    print("Python yorumlayıcınız bu programı kullanamaz!")
    exit(1)


class ScriptAl(HTMLParser):

    def reset(self):
        self.scriptler = []
        self.script_ici = False
        HTMLParser.reset(self)

    def handle_starttag(self,tag,ozellikler):

        if tag == "script":
            for anahtar,deger in ozellikler:
                if anahtar == "type" and deger == "text/javascript":
                    self.script_ici = True

    def handle_endtag(self,tag):
        if tag == "script" and self.script_ici:
            self.script_ici = False

    def handle_data(self,data):
        if self.script_ici:
            self.scriptler.append(data)

            from scriptal import ScriptAl
import urllib

parser = ScriptAl()
soket = urllib.urlopen("http://tr.myspace.com")
parser.feed(soket.read())
soket.close()

dosya = open("scriptler.txt","w")
for script in parser.scriptler:
    dosya.write("\n")
    dosya.write(script)
    dosya.write("\n\n")
dosya.close()
