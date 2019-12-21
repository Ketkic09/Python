class short:

    url = {}
    id = 1 
    def url_shortner(self,o_url):
        if o_url in self.url:

            self.id = self.url[o_url]
            url_shortner = self.id
            
        else :
        
            self.url[o_url] = self.id
            url_shortner = self.id
            self.id+=1
        self.url[o_url] ="short_url.com/"+str(url_shortner)
        return "short_url.com/"+str(url_shortner)
        

    def show(self):
        x = int(input("1 you want short url 2 you want original url "))
        if x==1:
            u = input("Enter the original url")
            print("The short url is ",self.url[u])
        elif x==2:
            u = input("Enter short url"+"\n")
            print("The original url is "+"\n")
            for i in self.url :
                if self.url[i]==u:
                    print(i)

c = 0
s = short()
while c!=3:
    
    print(" enter 1 url shortner 2 diaplay  3 exit")
    c = int(input("Your choice"))
    if c == 1:
        o = input("Enter the url ")
        print("The short url is ",s.url_shortner(o))
    
    elif c == 2:
        s.show()
   
    elif c>3 :
        print("Invalid")





