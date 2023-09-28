#Compare activity within next 30 second period, every 10 seconds?

'''
CONVERT 0:00 into seconds!!!?

time = 0

for time < stream_len

    check number of messages from time to time + 30 seconds

    increment time by + 10 seconds

    store frequencies in a list

compare the list and the highest x frequency compared to the average frequency is a hype moment

'''

def get_moments(collection):

    dict = {}

    time = 0

    q = {}
    sort_field = "time_in_seconds"
    final_document = collection.find_one(q, sort=[(sort_field, -1)])
    stream_len = final_document["time_in_seconds"]

    while(time < stream_len):
        
        start_time = time
        # end_time = time + 30
        end_time = time + 20

        query = {
            "time_in_seconds": {"$gte": start_time, "$lte": end_time}
        }
        count = collection.count_documents(query)
        dict[time] = count

        time += 10

    return dict


def get_hype_moments(moments_dict, stream_url):

    sorted_counts = sorted(moments_dict.values(), reverse=True)
    top_1_percent_index = int(0.01 * len(sorted_counts))
    threshold = sorted_counts[top_1_percent_index]
    
    # Filter the moments based on the threshold
    stream_url="https://www.youtube.com/watch?v=-p7XP7XAyco"
    top_moments = {
        seconds_to_hms(time): f"{stream_url}&start={time}" #Need to have input url instead
        for time, count in moments_dict.items() if count >= threshold

    }    
    return top_moments


def seconds_to_hms(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# INCOMPLETE AND UN-NEEDED
# def get_time_seconds(document):
    
#     total_time = 0

#     time_stamp = document["time_stamp"].split(":")
#     time_stamp = [int(i) for i in time_stamp]
    
#     l = len(time_stamp)
    
#     index = 0 #used to trace list from beginning to end

#     #multiples time by minutes or hours depending
#     while(l > 1):
#         time_stamp[i] = 60**(l-index)
#         index += 1

#     for num in time_stamp:
#         time += num
    
#     return time