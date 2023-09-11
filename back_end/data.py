import json

f = open("./jsons/chat2.json", "r", encoding='utf-8')
data = json.load(f)

# print(data[0]["author"]["badges"][0]["title"])
for message in data:


    # time_stamp = message['time_text'].split(":")
    # time_stamp = [int(i) for i in time_stamp]


    # # stream_len_str = message['time_text'].replace(":","")
    # # time_stamp = int(stream_len_str)
    # total_time = 0
    
    # l = len(time_stamp)
    
    # index = 0 #used to trace list from beginning to end

    # #multiples time by minutes or hours depending
    # while(index < l):
    #     time_stamp[index] *= 60**(l-index)
    #     print(time_stamp[index])
    #     index += 1

    # for num in time_stamp:
    #     total_time += num
    



    document = {
    "message_id": message["message_id"],    
    "time_stamp": message["time_text"],
    "time_in_seconds": message["time_in_seconds"],
    "name": message['author']['name']
    
    } 







    if "badges" in message["author"] and len(message["author"]["badges"]) > 0:
        badge = message["author"]["badges"][0]
        document["title"] = badge["title"] if "title" in badge else "Not found"
    else:
        document["title"] = "Not found"

    print(document)

   
# print(data[0]['time_text'])



# print(f.read())
# lines = []
# for line in f:
#     lines.append(line)

# for message in lines:
#     print(message[0:8])