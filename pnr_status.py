import urllib2
import urllib
import ipdb

send_to_list = ['8050326214']
api_key = "12345"

def getPNR(pnr):
    req = urllib2.Request("http://api.railwayapi.com/pnr_status/pnr/"+pnr+"/apikey/"+api_key+"/")
    response = urllib2.urlopen(req)
    #ipdb.set_trace()
    response_dict = eval(response.read().replace("\n", ""))
    if response_dict["error"] == False :
        trainNumber = response_dict["train_num"]
        trainName = response_dict["train_name"]
        dateOfJourney = response_dict["doj"]
        fromStation = response_dict["boarding_point"]["name"]
        toStation = response_dict["to_station"]["name"]
        pnrStatus = response_dict["passengers"][0]["current_status"]
        message = "Train No :" + trainNumber + "\n" + "Train Name : " + trainName + "\n" + "DOJ : " + dateOfJourney + "\n" \
                  + "From : " + fromStation + "\n" + "To : " + toStation + "PNR Status : " + pnrStatus
        sendMessage(message)
        return

def sendMessage(message):
    for i in send_to_list:
        str1 = 'SendMessage'
        send_to= i
        message = urllib.quote(message)
        url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=SendMessage&send_to="+send_to+"&msg="+message+"&msg_type=TEXT&userid=2000123765&auth_scheme=plain&password=29Q1xu8LO+&v=1.1&format=text"
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        response = response.read()
        print response


getPNR('568978')