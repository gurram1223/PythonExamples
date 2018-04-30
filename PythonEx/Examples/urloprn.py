from urllib.request  import urlopen
#with block: to manage resource returned by url since under the hood, fetching the resource from the web require os sockets and such like

#with stmt calls urlopen function and binds the response to a variable named story
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_word=[]
        for line in story:
        #line_words=line.split()
            line_words=line.decode('utf_8').split()
            for word in line_words:
                story_word.append(word)
    return story_word          
    
    #print(story_word) 
    '''for word in story_word:
        print(word)
        fetch_words()'''

def print_words(story_word):              
    for word in story_word:
        print(word)
        
def main():       
    words=fetch_words()
    print_words(words)
    
if __name__=='__main__':
    main()
    
'''import sys
    a=sys.argv[1]    --> for cmd line args'''
