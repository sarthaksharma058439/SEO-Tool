from tkinter import *
import tkinter as tk
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import urllib.request
import re


root=Tk()
root.title('Search Engine Optimizer')
root.geometry('1600x800+0+0')
root.configure(background='#2E86C1')

label=Label(root,text="Search Enginer Optimizer",font=('arial',50,'bold'),bg='#2E86C1')
label.grid(row=0,column=0)

label2=Label(root,text="    Powerful Next-Generation Tool For Search Engine Optimization At Your Fingertips.",font=('arial',25,'bold'),bg='#2E86C1')
label2.grid(row=1,column=0)

label3=Label(root,text="Analyze Your Website And Find Out The Issue And Fix It By Our Suggestions ",font=('arial',15,'bold'),bg='#2E86C1')
label3.grid(row=2,column=0)

label5=Label(root,text="____________________________________________________________________________",font=('arial',25,'bold'),bg='#2E86C1')
label5.grid(row=3,column=0)


label4=Label(root,text="",font=('arial',15,'bold'),bg='#2E86C1')
label4.grid(row=4,column=0)

label5=Label(root,text="",font=('arial',15,'bold'),bg='#2E86C1')
label5.grid(row=5,column=0)


label5=Label(root,text="Website URL Here",font=('arial',15,'bold'),bg='#2E86C1')
label5.grid(row=6,column=0)

entry1=Entry(root,width=150)
##entry.insert(END, 'Website URL Here')
entry1.grid(row=7,column=0)

label6=Label(root,text="",font=('arial',5,'bold'),bg='#2E86C1')
label6.grid(row=8,column=0)


label5=Label(root,text="Keyword Here",font=('arial',15,'bold'),bg='#2E86C1')
label5.grid(row=9,column=0)

entry2=Entry(root,width=50)
##entry.insert(END, 'Website URL Here')
entry2.grid(row=10,column=0)

label6=Label(root,text="",font=('arial',5,'bold'),bg='#2E86C1')
label6.grid(row=11,column=0)

button=Button(root,text="Analyze",font=('arial',10,'bold'),bg='#014c02',fg='white',command=lambda:geturl())
button.grid(row=12,column=0)

label7=Label(root,text="",font=('arial',15,'bold'),bg='#2E86C1')
label7.grid(row=13,column=0)

output=Text(root,width=100,height=13)
output.grid(row=14,column=0)

button2=Button(root,text="Clear",font=('arial',10,'bold'),bg='#014c02',fg='white',command=lambda:reset())
button2.grid(row=15,column=0)

def reset():
    output.delete(1.0,END)

def geturl():
    url=entry1.get()
    keyword=entry2.get()

    try:
        req=Request(url,headers={'User-Agent':'Mozilla/6.0'})
        html=urlopen(req)
    except HTTPError as e:
        print(e)

    data = BeautifulSoup(html,"html.parser")

    def seo_title_found(keyword,data):
        if data.title:
            if keyword in data.title.text.casefold():
                status="keyword found"

            else:
                status="keyword not found"

        else:
            status="no title found"
            
        return status

    def seo_title_stop_words(data):
        words=0
        list_words=[]
        if data.title:
            with open('stopwords.txt','r') as f:
                for line in f:
                    if re.search(r'\b'+line.rstrip('\n')+r'\b',data.title.text.casefold()):
                        words+=1
                        list_words.append(line.rstrip('\n'))

            if words>0:
                stop_words="we found {} stop words in your title. you should consider removing them.{}".format(words,list_words)
            else:
                stop_words="we found no stop words in the title. good work!"
        else:
            stop_words="we could not find the title"
        return stop_words

    def seo_title_length(data):
        if data.title:
            if len(data.title.text)<60:
                length="your length is under the maximum suggested lenght of 60 characters. your title lenght is {} ".format(len(data.title.text))
            else:
                length="your length is over the maximum suggested length of 60 characters. your title lenght is {} ".format(len(data.title.text))

        else:
            length="no title is found"
        return length
    def seo_title_overdo(keyword,data):
        if data.title:
             result=data.title.text.split()
             count=result.count(keyword)+1
             if count<3:
                 keyword_overdo="The keyword {} occurs: ".format(keyword) + str(count)+" times. Title not overdo with keyword.Good work!"
        else:
            keyword_overdo="keyword overdo. keyword occur:"+str(count)+"times. You are suggested to reduce occurence of keyword from title"
        return keyword_overdo
                
    def seo_description_length():
        
        page_description=urllib.request.urlopen(url)
        description=BeautifulSoup(page_description.read(),"html.parser")
        metas=description.find_all('meta')
        
        description_len=([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])
        str1=''.join(str(e) for e in description_len)
        description_len2=len(str1)
        
        if len(str1)<50:
            description="Your description length is under 50 character. You are suggested to increase the length of description"
        if len(str1)>300:
            description_length="Your description length is over 300 character. You are suggested to reduce the length of description"
        else :
            description_length="Your description length is {} . Good Work!".format(len(str1))

        return description_length

    def seo_description_overdo(keyword):
        page_description=urllib.request.urlopen(url)
        description=BeautifulSoup(page_description.read(),"html.parser")
        metas=description.find_all('meta')
        
        description_len=([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])
        str1=''.join(str(e) for e in description_len)
        result=str1.lower().split()
        count=result.count(keyword)
        if count<3:
            counter="your description contain kewords {} {} times. Good work!".format(keyword,count)
        else:
            counter="your description contain keyword {} {} times. You are suggested to reduce occurence of keyword from description".format(keyword,count)
        
        return counter

    def seo_url(url):

        if url:
            if keyword in url:
                slug="your keyword {} was found in your slug".format(keyword)
            else:
                slug="your keyword {} is not found in your slug.It is suggested to add your keyword to your slug".format(keyword)

        else:
            slug="no url was returned"

        return slug

    def seo_url_https(url):

        if url:
            a="https"
            
            if a in url:
              https="https found in your url.Good work! "
            else:
                https="https not found . It is suggested to convert into http(for security purpose of data)"
        else:
            https="url not found"

        return https

    def seo_url_length(url):
        if url:
            if len(url)<100:
                url_length="your url is less than 100 character maximum suggested length. good work!"
            else:
                url_length="your url length is over 100 character. Your url currently is {}. you should change this.".format(len(url))
        else:
            url_length="URL not found"
        return url_length

    def seo_h1(keyword,data):
        total_h1=0
        total_keyword_h1=0
        if data.h1:
            all_tags=data.find_all('h1')
            for tag in all_tags:
                total_h1+=1
                tag=str(tag.string)
                if keyword in tag.casefold():
                    total_keyword_h1+=1
                    h1_tag="found keyword in h1 tag.You have a total of {} H1 tags and your keyword was found in {} of them".format(total_h1,total_keyword_h1)
                else:
                    h1_tag="Did not found any keyword in h1 tag"
        else:
            h1_tag="no h1 tags found"

        return h1_tag

    out1=seo_title_found(keyword,data)
    out2=seo_title_stop_words(data)
    out3=seo_title_length(data)
    out4=seo_title_overdo(keyword,data)
    out5=seo_description_length()
    out6=seo_description_overdo(keyword)
    out7=seo_url(url)
    out8=seo_url_https(url)
    out9=seo_url_length(url)
    out10=seo_h1(keyword,data)

    output.insert(0.0,out1+"\n"+"\n")
    output.insert(0.0,out2+"\n")
    output.insert(0.0,out3+"\n")
    output.insert(0.0,out4+"\n")
    output.insert(0.0,out5+"\n")
    output.insert(0.0,out6+"\n")
    output.insert(0.0,out7+"\n")
    output.insert(0.0,out8+"\n")
    output.insert(0.0,out9+"\n")
    output.insert(0.0,out10+"\n")

   

root.mainloop()
