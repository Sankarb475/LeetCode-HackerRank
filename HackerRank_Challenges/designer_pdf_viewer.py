# solution of https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    maxheight = 0
    for i in word:
        index = ord(i) - 97
        if h[index] > maxheight:
            maxheight = h[index]
    return maxheight * len(word)
