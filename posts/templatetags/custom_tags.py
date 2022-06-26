from django import template

from django.template.defaultfilters import stringfilter
import re
from django.utils.text import Truncator

register = template.Library()

# register filter
# is_safe is for telling Django that if a “safe” string is passed into your filter, the result will still be “safe” and if a non-safe string is passed in, Django will automatically escape it, if necessary.
@register.filter(is_safe=True)
# only accepts string as the first argument.
@stringfilter                 
def removelinebreaks(text, num):
    # case insensitive matching of '&nbsp;' non-breaking space
    text= re.sub('&nbsp;', '', text, flags=re.IGNORECASE) 
    #remove space, tabs, and newlines zero or more times
    text= re.sub("<p>\s*</p>","", text, flags=re.MULTILINE) 
    # remove <br> tag.
    text= re.sub("<br>","", text)

    # truncate the text
    if len(text) < num:
        return Truncator(text).chars(num)
    return Truncator(text).chars(num) + '...'

@register.filter(is_safe=True)
@stringfilter
def getonlytext(text):
    text = ''.join( x for x in text if x not in '"')
    for i in range(0, text.count('<')):
        start = text.find('<')
        end = text.find('>')
        if end == -1:
            break
        text = text[:start]+text[end+1:]
    return text

@register.filter(is_safe=True)
@stringfilter
def url_editor(text):
    reference = "/posts/" # 찾는 데 기준이 되는 텍스트
    ref_len = len(reference)
    posts_location = text.find(reference)
    # print("posts_location : " + str(posts_location))
    head_part = text[:posts_location+ref_len] # www.homepage/posts/ 까지 자름
    # print("head_part : " + head_part)
    tail_part_raw = text[posts_location+ref_len:] # ***/24/edit (posts/ 뒷부분)
    # print("tail_part_raw : " + tail_part_raw)
    cutting_location = tail_part_raw.find("/")
    # print("cutting_location : " + str(cutting_location))
    if cutting_location != -1:
        tail_part = tail_part_raw[:cutting_location] # *** 뒤에 /가 존재할 경우(***/aaa/ddd) 거기서 끊음; ***
    else:
        tail_part = tail_part_raw # *** 뒤에 /가 존재하지 않을 경우(***) 아무것도 수행하지 않음
    return head_part + tail_part + "/uploads"