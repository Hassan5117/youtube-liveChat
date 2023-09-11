# from chat_downloader import ChatDownloader
# import subprocess

# #I made it now so that it prints the formatted message to chat.txt

# # url = 'https://www.youtube.com/watch?v=-p7XP7XAyco'
# # chat = ChatDownloader().get_chat(url, output="./chat5.txt", format="24_hour")       # create a generator
# # for message in chat:                        # iterate over messages
# #     # chat.print_formatted(message) # print the formatted message
# #     print(chat)

# # print(dir(chat))
# # print(chat.video_type)

# user_url = input("Please enter the YouTube live stream URL: ")

# # command = ['chat_downloader', 'https://www.youtube.com/watch?v=-p7XP7XAyco', '--output', 'chat2.json']
# command = ['chat_downloader', user_url, '--output', 'chat11.json']
# result = subprocess.run(command, capture_output=True, text=True)




# #chat_downloader https://www.youtube.com/watch?v=jfKfPfyJRdk --output chat.json



from chat_downloader import ChatDownloader

def capture_chat_data(stream_url):
    # Capture chat messages using ChatDownloader
    chat = ChatDownloader().get_chat(stream_url)
    
    # Process chat messages and extract the desired fields
    chat_data = []
    for message in chat:
        document = {
            "message_id": message["message_id"], 
            "name": message['author']['name'],
            'message': message['message'],
            "time_stamp": message['time_text'],
            "time_in_seconds": message["time_in_seconds"]
        }
        chat_data.append(document)
        
    return chat_data