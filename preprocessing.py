import requests
import pandas as pd
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)
df = pd.read_csv("/home/dikshith/Desktop/grafana_data_export.csv",sep=",")
msg = list(df["text"])
# phata=[]
# ner=[]
resp=[]
mmsg=[]
senti = []
score=[]

count=0
for string in msg:
    # if count>10:
    #     break
    try:
        string = string.rstrip()
        string = remove_non_ascii(string)
        # print(string)
        # d=[]
        url = "http://0.0.0.0:5000/sentiment"
        
        payload = "{\"text\":\""+string+"\"}"
        headers = {
                    'content-type': "application/json",
                    'cache-control': "no-cache",
                    'postman-token': "32493300-0f2e-f534-4f87-1fd7be1ab437"
                    }
        response = requests.request("POST", url, data=payload, headers=headers)
        # print(response.text)
        response = response.json()
        print (response)
        # print response["attributes_per_text"]
        # ner.append(response["attributes_per_text"][0]["ner"])
        resp.append(response)
        # print response
        print (response["score"])
        print (response["sentiment"])
        senti.append(response["sentiment"])
        score.append(response["score"])
        mmsg.append(string)
        # em = []
        # for e in response["emotion_mapping"]:
        #     em.append(e["emotion"])
        #op_time.append(response["time"])
        # emotion.append(" | ".join(em))
        print("check")
        #output_file.write(output_string)
        count+=1
    except:
        # response = response.json()
        resp.append("CRASHED")
        mmsg.append(string)
        senti.append("CRASHED")
        print (string)
        print("check except")
        count+=1
        pass

# print phata
# print len(mmsg),len(resp),len(emotion)
df_op = pd.DataFrame({"msg":mmsg,"sentiment":senti,"score":score})

df_op.to_csv("op_senti.csv",encoding='utf-8')