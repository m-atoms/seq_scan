# inserts html tags directly before and after a specific character
# in the protein sequence as specified by index argument
def insert_tags(idx, seq):
    # find index to insert tags at - account for inserted tags
    insert_idx = itr(idx, seq)
    
    # string slicing
    #         [start of str up to char)   <open tag>   [character in motif]   <close tag>   [char+1 to end of string]
    tagd = seq[: (insert_idx)] + "<strong>" + seq[insert_idx] + "</strong>" + seq[(insert_idx+1) :]
    
    return tagd

# iterates over the sequence accounting for html tags
# in order to preserve original sequence char indexes
def itr(idx, seq):
    
    # track true_idx (characters protein in sequence) and offset (characters in tags)
    offset = 0
    true_idx = 0
    
    # iterate through seq/tag chars until motif idx is found, regardless of offset added by tags
    while (true_idx != idx) or (not seq[true_idx+offset].isupper()):
        if seq[true_idx+offset].isupper():
            true_idx+=1
        else:
            offset+=1
    
    return true_idx + offset

# iterate over each character, build substrings incrementally,
# then write substring to list when 10 uppercase chars have been found
def split(num, seq_tagd):
    seq_seg = []
    ctr = 0
    seg = ""
    
    for idx, char in enumerate(seq_tagd):
        if char.isupper():
            ctr+=1
            if (ctr == num) or (idx == (len(seq_tagd)-1)):
                ctr = 0
                seg += char
                seq_seg.append(seg)
                seg = ""
            else:
                seg += char
        elif (idx == (len(seq_tagd)-1)):
            seg += char
            seq_seg.append(seg)
        else:
            seg += char
    return seq_seg

# use hijacked stdout and print straight to output file
# html doesn't care about indents or whitespace so neither do I
# could this have been done more elegantly? yes, but it does the job and I'm tired
def html_gen(seq_seg):
    print("<html>")
    print("<head>")
    # define style
    print("<style>")
    print("* {font-family:'Courier New';}") #Lucida Console is another good monospace font
    print("strong {color:red;}") # matches appear bold and red
    print(".num {text-align:right;}") # numbers are aligned to the right of each cell
    print(".seq {font-size:18px;}") # increase font from default (16px)
    print("</style>")
    print("</head>")
    #define table
    print("<body>")
    print("<table>")
    print("<tr>")
    # first row of numbering
    for i in range(0,5):
        print("<td class='num'>{}</td>".format((i+1)*10))
    print("</tr>")
    # create table rows for sequence and corresponding numbers
    print("<tr>")
    for idx, seg in enumerate(seq_seg):
        if idx > 0 and idx % 5 == 0:
            print("</tr>")
            print("<tr>")
            for i in range(0,5):
                print("<td class='num'>{}</td>".format((idx+(i+1))*10))
            print("</tr>")
            print("<tr>")
        print("<td class='seq'>{}</td>".format(seg))
    print("</tr>")
    print("</table>")
    print("</body>")
    print("</html>")