from vendor import web
import simplejson, urllib

urls = (
  '/reinstall', 'index',
)

UPDATE_URL = "https://versioncheck.addons.mozilla.org/update/VersionCheck.php?"

# Hardcode from now
inputjson = '{"inspector@mozilla.org":{"name":"DOM Inspector", "version":"2.0.1", "icon":"chrome://mozapps/skin/xpinstall/xpinstallItemGeneric.png"}, "firenomics@overstimulate.com":{"name":"Firenomics", "version":"0.1", "icon":"chrome://mozapps/skin/xpinstall/xpinstallItemGeneric.png"}, "{8f8fe09b-0bd3-4470-bc1b-8cad42b8203a}":{"name":"Live HTTP headers", "version":"0.14", "icon":"chrome://livehttpheaders/skin/img/Logo_32.png"}, "taboo@runningfrombears.com":{"name":"Taboo", "version":"0.5.9", "icon":"chrome://taboo/skin/logo.png"}}'

# We should get that from the user agent
os = "Linux"
browserver = "3.0.4"
locale = "en-US"

def getInstallJSON():
  myjson = simplejson.loads(inputjson)
  result = []
  for id in myjson:
    params = {
      "reqVersion": "2",
      "id": id,
      "version": "0.0.1",
      "appID": "{ec8030f7-c20a-464f-9b0e-13a3a9e97384}",
      "appVersion": browserver,
      "appOS": os,
      "locale": locale,
      "currentAppVersion": browserver
    }
    url = UPDATE_URL + urllib.urlencode(params)
    myjson[id]["guid"] = id
    myjson[id]["xpiurl"] = url
  return myjson
