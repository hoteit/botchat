from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .chatbotform import PostForm
from datetime import datetime
import parsedatetime as pdt
import re
import nltk
from stop_words import get_stop_words
from nltk.corpus import stopwords
from string import punctuation
from .date import dateparser
# Create your views here.
def parser(time_string):

    cal = pdt.Calendar()
    now = datetime.now()
    return cal.parseDT(time_string, now)[0]

def ajax_dateparse(request):
    # It allows us to handle date before posting all form data
    # so we can format the date and then pass it to the input in the form
    if request.method == 'POST':
        text = request.POST.get('text')
        text = dateparser(text)
    return JsonResponse({'content': text})


def post_list(request):
    if request.method == "POST":
        _allposts = Post.objects.all()
        form = PostForm()
        parsed= finparser(request.POST.get("full_note"))
        val = (int) (request.POST.get("dc"))
        if(val==100000):
            Post.objects.create(author=len(_allposts), name=request.POST.get("name"), issue_or_change=request.POST.get("issue_or_change"),
                full_note = parsed['raw'] , date_field  = parser(parsed['date']), cid = parsed['id'], processed_note = parsed['processed'])
        else:
            Post.objects.create(author=len(_allposts), name=request.POST.get("name"), issue_or_change=request.POST.get("issue_or_change"),
                full_note = parsed['raw'] , date_field  = parser(request.POST.get("date_field")), cid = parsed['id'], processed_note = parsed['processed'])
        allposts = Post.objects.all()
        return render(request, 'chat/post_list.html',{'posts': allposts})
    else :
        allposts = Post.objects.all()
        form = PostForm()
        return render(request, 'chat/post_list.html', {'posts': allposts , 'form': form})


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

nltk.download('stopwords')

def finparser(time_string):
    cal = pdt.Calendar()
    now = datetime.now()
    dic={}
    dic['raw']=time_string
    dic['date']=dateparser(time_string)
    id=re.findall(r'[A-Z]{2,5}[0-9]{3}[0-9]*', time_string)
    if(len(id)==0):
        dic['id']='NA'
    else:
        dic['id']=id[0]

    stop_words = list(get_stop_words('en')) #About 900 stopwords
    nltk_words = list(stopwords.words('english')) #About 150 stopwords
    add_words=['i',':','one','two','three','four','five','six','seven','pm','ago','day','days','am','.',',','eight','nine', 'ten','hour','hours','min','mins','minute','minutes','second','seconds','yday','ysterday','yesterday','morning','afternoon','night','evening','today','tomorrow','tommorrow','noon','midnight','next','week','weeks','month','months','year','years','ago','monday','tuesday','wednesday','right','thursday','friday','saturday','sunday']
    stop_words.extend(nltk_words)
    stop_words.extend(add_words)
    time_string=re.sub(r'[A-Z]{2,5}[0-9]{3}[0-9]*','',time_string)
    time_string=re.sub(r'[0-9]*','',time_string)
    dic['processed']=[w for w in strip_punctuation(time_string).lower().split() if not w in stop_words]
    dic['processed']=' '.join(dic['processed'])
    return dic
