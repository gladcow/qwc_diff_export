"""
qwertycoind JSONRPC interface
"""
import requests
import json

class QwertycoindJsonApi():
    def __init__(self, url):
        self.url = url

    def rpc_command(self, method,  params):
        # standard json header
        headers = {'content-type': 'application/json'}
        # add standard rpc values
        if not params is None:
            params.update({"jsonrpc": "2.0", "id": "0"})
        response = requests.post(
            self.url + "/" + method,
            data=None if params is None else json.dumps(params),
            headers=headers)

        return response.json()

    def getinfo(self):
        return self.rpc_command("getinfo", None)

    def getheight(self):
        reply = self.rpc_command("getheight", None)
        if reply["status"] != "OK":
            raise Exception(reply["status"])
        return int(reply["height"])

    def getblockheaderbyheight(self, height):
        params = {
            "method": "getblockheaderbyheight",
            "params": {"height": height}
        }
        reply = self.rpc_command("json_rpc", params)
        if reply["result"]["status"] != "OK":
            raise Exception(reply["status"])
        return reply["result"]["block_header"]
