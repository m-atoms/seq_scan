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