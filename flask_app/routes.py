import requests, json
from . import app, ibm_url, ibm_url_get, headers

@app.route('/')
def hello_world():
    data = json.dumps({"text": 
    [ "He won critical acclaim for his directorial feature debut A Star Is Born in 2018.",
    "But for his next project, Bradley Cooper is letting somebody else call the shots.",
    "The actor, 45, was spotted over the weekend filming on location in LA's San Fernando Valley for filmmaker Paul Thomas Anderson.",
    "Plot details are scarce but the story centers around a high school student who is also a successful child actor.",
    "To date, Cooper is the only known name attached to the drama.",
    "This will be Anderson's fourth film set in the San Fernando Valley following Boogie Nights, Magnolia and Punch Drunk Love.",
    "Cooper was dressed in a loose-fitting white shirt and white cotton flares with brown shoes.",
    "He sported a shaggy brown wig and a full beard and wore a medallion necklace, looking very different from his dapper day-to-day appearance.",
    "The action took place in a gas station and the actor was seen at various times with a windscreen squeegee or a gas canister in hand.",
    "At one point, he appeared to be angrily threatening a young man with gasoline and a lighter. ",
    "He was joined in the scenes by a young actor and actress who were with him in the cab of a box truck.",
    "He was also seen in conversation with crew as scenes were set up.",
    "The production was clearly abiding by strict protocols as the coronavirus pandemic continues."]})
    response = requests.post(url=ibm_url, 
                data=data,
                headers=headers)
                
    return response.json()