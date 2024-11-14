import re

def determine_format_from_date(date):
    date_parts = date.split("/")
    # print(date_parts)
    if int(date_parts[1]) > 12 and int(date_parts[0]) > 12:
        return "invalid date format"
    elif int(date_parts[1]) > 12:
        return "MM/DD/YYYY"
    elif int(date_parts[0]) > 12:
        return "DD/MM/YYYY"
    return "Ambiguous"

def determine_context_clue(context_before, context_after, british_words, american_words, before_keywords, after_keywords):
    
    combined_context = context_before + context_after
    for word in british_words:
        if word in combined_context:
            return "DD/MM/YYYY format (British English context)"
    for word in american_words:
        if word in combined_context:
            return "MM/DD/YYYY format (American English context)"

    found_before = any(kw in context_before for kw in before_keywords)
    found_after = any(kw in context_before for kw in after_keywords)

    if found_before:
        return "DD/MM/YYYY context: registration deadline or due date"
    elif found_after:
        return "MM/DD/YYYY context: event or report date"
    else:
        return "Ambiguous"

def date_format(content):
    ans = []
    dates = re.findall(r'\d{1,2}\/\d{1,2}\/\d{1,4}', content)
    # print(dates)
    british_words = ["colour", "favour", "programme", "organisation", "metre", "centre", "defence", "licence", 
                     "telly", "recognise", "analyse", "autumn", "lorry", "petrol"]
    american_words = ["color", "favor", "program", "organization", "meter", "center", "defense", "license", 
                      "labor", "recognize", "analyze", "fall", "truck", "gasoline"]
    before_keywords = ["registration deadline", "starts on", "deadline", "due date", "conference", "begins", "starts"]
    after_keywords = ["conference", "due on" , "event", "final report", "ends on", "report", "held", "scheduled", "ends", "finishes"]
    # khubaib = False
    for date in dates:
        format_clue = determine_format_from_date(date)
        if format_clue == "Ambiguous":
            context_before = content.split(date)[0]
            context_after = content.split(date)[1]
            print(context_before, date)
            print(context_after, date)
            format_clue = determine_context_clue(context_before, context_after, british_words, american_words, before_keywords, after_keywords)
            # print(format_clue)
        # if format_clue != "Ambiguous" and format_clue != 'invalid date format':
        #     khubaib = True
        #     ans.append((date, format_clue))
        #     return ans,khubaib
        ans.append((date, format_clue))
    return ans
    # return ans,khubaib

data = []
# khubaib = False
with open('date_format_dd_mm_yyyy.txt', 'r') as file1:
    lines = file1.readlines() 
    for line in lines:
        line = line.strip()
        if line:
            # x,khubaib = date_format(line)
            x = date_format(line)
            if len(x) == 2:
                data.append(x[0])
                data.append(x[1])
            elif len(x) == 1:
                data.append(x[0])
        # if khubaib == True:
        #     break

print(data)

def write(tokens, file_dest):
    with open(file_dest, 'w') as file:
        for token in tokens:
            file.write(str(token )+ '\n')
            
write(data, "Q1_output.txt")
print("DONE")