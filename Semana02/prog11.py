with open('img1.jpeg', 'rb') as rf:
    with open('img2.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunck = rf.read(chunk_size)
        while len(rf_chunck) > 0:
            wf.write(rf_chunck)
            rf_chunck = rf.read(chunk_size)