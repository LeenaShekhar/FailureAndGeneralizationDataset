def correct(src, target):
    '''
    Return True if the target is a valid output given the source
    Args
        src (str)  
        target (str)
    formats should match those in the datafiles
    '''

    self.grammar_vocab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AS', 'BS', 'CS', 'DS', 'ES', 'FS', 'GS', 'HS', 'IS', 'JS', 'KS', 'LS', 'MS', 'NS', 'OS']
    inpt = src.split()
    pred = target.split()
    is_correct = True 
    #Check if the length is correct
    length_check = True if len(pred) == 3 * len(inpt) else False
    #Check if everything falls in the same bucket, and there are no repeats
    if length_check:
        for idx, inp in enumerate(inpt):
            vocab_idx = grammar_vocab.index(inp) + 1                              
            span = pred[idx*3:idx*3+3]
            span_str = " ".join(span)
            if not all(int(item.replace("A", "").replace("B", "").replace("C", "").split("_")[0]) == vocab_idx for item in span \
               or not ("A" in span_str and "B" in span_str and "C" in span_str):
                all_correct = False
                break
            
    return all_correct

