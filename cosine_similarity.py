#Cosine similarity between two sentences

def Counter(m): 
	j= dict()
	for word in m:
		if word in j:			#word found-- increment count
			j[word]=j[word]+1
		else:				#word not found. Add to dictionary
			j.update({word:1})
	return j

def sqr(a):

     i=0.000
     while((i**2)<a):
     	i=i+0.000001	    
     return i
   
def take_cosine(vec1, vec2):

     intersection = set(vec1.keys()) & set(vec2.keys())
     n = sum([vec1[x] * vec2[x] for x in intersection]) #numerator
     
     sum1 = sum([vec1[x]**2 for x in vec1])
     sum2 = sum([vec2[x]**2 for x in vec2])
     d = sqr(sum1) * sqr(sum2)				#denominator

     if not d:
        return 0.0
     else:
        return float(n) / d

def text_to_vector(text):
     
     words =text.split()
     return Counter(words)

sentence1 = raw_input("Enter the first sentence\n")
sentence2 = raw_input("Enter the second sentence\n")

vector1 = text_to_vector(sentence1)
vector2 = text_to_vector(sentence2)

cosine = take_cosine(vector1, vector2)

print 'Cosine similarity :', round(cosine,5)
