from errbot import BotPlugin, botcmd
import json
import urllib.request

class DolARG(BotPlugin):
    """ placeholder """

    @botcmd
    def dolar(self, msg, args):
        user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"
        url = "http://contenidos.lanacion.com.ar/json/dolar"
        headers={"User-Agent":user_agent,'Accept-Encoding':'utf-8'}

        request = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(request).read().decode("utf-8")

        data_string = res.replace('dolarjsonpCallback(', '')
        data_string2 = data_string.replace(');', '')

        data = json.loads(data_string2)

        return "Compra: " + data["CasaCambioCompraValue"] + " | " + "Venta: " + data["CasaCambioVentaValue"]
